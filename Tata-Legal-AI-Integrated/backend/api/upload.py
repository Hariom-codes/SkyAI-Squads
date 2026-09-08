from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from uuid import uuid4

from services.ocr_service import extract_text_from_pdf, get_pdf_page_count
from services.parser_service import parse_clauses
from services.rag_service import retrieve_relevant_knowledge_batch
from services.ai_service import analyze_clauses_fast, summarize_document
from services.approval_service import get_review, add_audit_event
from api.auth import current_user_from_request

router = APIRouter()


@router.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    user = current_user_from_request(request)
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file was provided.")
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        pdf_bytes = await file.read()
        if len(pdf_bytes) > 15 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="PDF exceeds the 15 MB upload limit.")
        if not pdf_bytes:
            raise HTTPException(status_code=400, detail="The uploaded PDF is empty.")

        document_id = f"DOC-{uuid4().hex[:12].upper()}"
        add_audit_event(document_id, "Document Uploaded", f"{file.filename} uploaded for analysis", user["display_name"], user["role"])
        page_count = get_pdf_page_count(pdf_bytes)
        extracted_text = extract_text_from_pdf(pdf_bytes)
        add_audit_event(document_id, "OCR Completed", f"Text extracted from {page_count} page(s)", user["display_name"], user["role"])
        if not extracted_text.strip():
            raise HTTPException(status_code=422, detail="Could not extract text from the PDF.")

        clauses = parse_clauses(extracted_text)
        add_audit_event(document_id, "Document Parsed", f"{len(clauses)} clauses identified", user["display_name"], user["role"])
        if not clauses:
            raise HTTPException(
                status_code=422,
                detail="No numbered legal clauses could be identified in the document. Make sure the PDF contains numbered clause headings such as '1. PARTIES'."
            )

        # Performance optimization: embed/retrieve all clauses in one batch, then
        # analyze them through a few parallel Gemini calls instead of one request per clause.
        knowledge_batches = retrieve_relevant_knowledge_batch([c.get("clause_text", "") for c in clauses], k=3)
        ai_items = []
        for i, clause in enumerate(clauses):
            retrieved = knowledge_batches[i] if i < len(knowledge_batches) else []
            ai_items.append({
                "clause_name": clause.get("clause_name", ""),
                "clause_text": clause.get("clause_text", ""),
                "knowledge": "\n\n".join(item.get("content", "") for item in retrieved),
            })

        analyses = analyze_clauses_fast(ai_items, batch_size=6)
        analyzed_clauses = []
        for index, clause in enumerate(clauses, start=1):
            retrieved = knowledge_batches[index - 1] if index - 1 < len(knowledge_batches) else []
            analysis = analyses[index - 1] if index - 1 < len(analyses) else {
                "clause_name": clause.get("clause_name", ""),
                "summary": "AI analysis could not be completed.",
                "risk_level": "Unknown", "confidence": 0, "risk_reason": "",
                "recommendation": "Please review this clause manually.",
            }
            sources = [{"source": item.get("source"), "page": item.get("page")} for item in retrieved]
            clause_id = f"clause-{index}"
            analyzed_clauses.append({
                **clause, "clause_id": clause_id, "analysis": analysis,
                "sources": sources, "human_review": get_review(document_id, clause_id),
            })

        add_audit_event(document_id, "Clauses Extracted", f"{len(analyzed_clauses)} clauses extracted for review", user["display_name"], user["role"])
        add_audit_event(document_id, "Knowledge Retrieval Completed", "Clauses compared against organizational knowledge base", user["display_name"], user["role"])
        document_summary = summarize_document(analyzed_clauses)
        levels = [c.get("analysis", {}).get("risk_level") for c in analyzed_clauses]
        confidence_values = [
            int(c.get("analysis", {}).get("confidence", 0))
            for c in analyzed_clauses
            if str(c.get("analysis", {}).get("confidence", "")).isdigit()
        ]
        high = levels.count("High")
        medium = levels.count("Medium")
        low = levels.count("Low")
        unknown = len(levels) - high - medium - low
        overall = document_summary.get("overall_risk") or ("High" if high else "Medium" if medium else "Low" if low else "Unknown")
        confidence = round(sum(confidence_values) / len(confidence_values)) if confidence_values else 0

        add_audit_event(document_id, "Risk Analysis Generated", f"{len(analyzed_clauses)} risk findings generated", "AI System", "AI")

        return {
            "document_id": document_id,
            "filename": file.filename,
            "message": "File uploaded and processed successfully",
            "page_count": page_count,
            "extracted_text": extracted_text,
            "clauses": analyzed_clauses,
            "contract_summary": document_summary.get("summary", ""),
            "risk_summary": {
                "overall": overall,
                "confidence": confidence,
                "high": high,
                "medium": medium,
                "low": low,
                "unknown": unknown,
                "total": len(analyzed_clauses),
            },
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the document: {str(e)}")
