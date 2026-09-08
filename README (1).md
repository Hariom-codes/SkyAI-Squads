# ⚖️ Tata Legal AI — Legal Document Intelligence System

> An AI-powered platform that reads, understands, and analyzes legal documents — extracting clauses, flagging risks, and generating recommendations, with a human always in the loop.

Developed by **Team SkyAI-Squads** as part of the AlmaBetter × IIT Patna Fellowship capstone project for **Tata Group**.

---

## 📌 Overview

**Tata Legal AI** simplifies and accelerates the review of legal documents. It processes legal PDFs and automatically extracts:

- 📄 Clauses
- 📝 Summaries
- ⚠️ Potential risks
- 📚 Supporting legal knowledge
- ✅ Recommendations

The system combines **PDF processing, OCR, text parsing, clause extraction, Retrieval-Augmented Generation (RAG), LangChain, Gemini Embeddings, ChromaDB, Google Gemini LLM, SQLite, FastAPI, React, and Docker** into a single end-to-end legal document intelligence platform — with **human review** built into the workflow.

---

## 🎯 Objective

Reduce the manual effort of reviewing lengthy legal documents by enabling users to:

- Upload legal documents
- Extract text from PDFs (including scanned ones via OCR)
- Parse and structure document content
- Identify important legal clauses
- Retrieve relevant legal knowledge
- Analyze clauses using Generative AI
- Identify potential risks and generate recommendations
- Review AI-generated results through human approval
- Store and retrieve processed results via a unique document ID

> 🧑‍⚖️ The system is **AI-assisted, not AI-decided** — human review remains central to the workflow.

---

## 🏗️ System Architecture

```
Frontend (React + Vite)
        │
        ▼
FastAPI Backend
        │
        ▼
PDF Processing → OCR / Text Extraction → Parsing → Clause Extraction
        │
        ▼
RAG Retrieval (ChromaDB + Gemini Embeddings)
        │
        ▼
Gemini LLM → Risk Analysis
        │
        ▼
Human Approval
        │
        ▼
SQLite Database → Result Retrieval → Frontend
```

---

## 🧠 Legal Knowledge Base (RAG)

A dedicated knowledge base of **20 legal PDF documents** powers the Retrieval-Augmented Generation pipeline, so the LLM reasons using real legal reference material instead of general knowledge alone.

```
20 Legal PDFs → Text Extraction → Chunking → Gemini Embeddings → ChromaDB → Semantic Search → Relevant Knowledge → Gemini LLM
```

- **Chunking:** Recursive text-splitting with contextual overlap
- **Embedding Model:** `gemini-embedding-001`
- **Vector DB:** ChromaDB
- **Orchestration:** LangChain

---

## 🔍 Core Workflow

| Step | Description |
|------|-------------|
| 1️⃣ Upload | User uploads a PDF via the React frontend → `POST /upload` |
| 2️⃣ Validation | File type, emptiness, and processability checks |
| 3️⃣ PDF Processing | Text extraction (or OCR for scanned docs) |
| 4️⃣ OCR | Tesseract OCR + pytesseract + pdf2image + Pillow |
| 5️⃣ Parsing | Text cleaning & structuring |
| 6️⃣ Clause Extraction | Document broken into individually analyzable clauses |
| 7️⃣ RAG Retrieval | Relevant legal knowledge fetched from ChromaDB |
| 8️⃣ AI Analysis | Gemini LLM generates summary, risk level, reason, recommendation |
| 9️⃣ Human Review | Approve / Reject / Edit / Escalate |
| 🔟 Persistence | Result stored in SQLite with a unique Document ID |

---

## 🧩 AI Output per Clause

- Clause Name
- Summary
- Risk Level
- Risk Reason
- Recommendation

---

## 👩‍⚖️ Human-in-the-Loop Review

AI output is **never treated as a final legal decision**. Reviewers can:

- View pending clauses
- ✅ Approve
- ❌ Reject
- ✏️ Edit
- 🚩 Escalate

**Statuses:** `Pending` · `Approved` · `Rejected` · `Escalated`

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend | React + Vite |
| Backend | Python + FastAPI |
| PDF Processing | pypdf |
| OCR | Tesseract OCR, pytesseract, pdf2image, Pillow |
| RAG Framework | LangChain |
| Embedding Model | gemini-embedding-001 |
| Vector Database | ChromaDB |
| LLM | Google Gemini |
| Database | SQLite |
| API | REST (FastAPI) |
| API Docs | Swagger / OpenAPI |
| Containerization | Docker |
| Frontend Deployment | Netlify |
| Backend Deployment | Render |

---

## 📡 API Endpoints

### Basic
```
GET /
GET /health
```

### Document Processing
```
POST /upload
GET  /documents/{document_id}
```

### Human Approval
```
GET  /approvals/pending
GET  /approvals/{clause_id}
POST /approvals/{clause_id}/accept
POST /approvals/{clause_id}/reject
PUT  /approvals/{clause_id}/edit
POST /approvals/{clause_id}/escalate
```

📖 Interactive Swagger docs available at: `http://localhost:8000/docs`

---

## 📂 Project Structure

```
Tata-Legal-AI/
│
├── backend/
│   ├── api/
│   │   ├── upload.py
│   │   └── human_approval.py
│   │
│   ├── services/
│   │   ├── ocr_service.py
│   │   ├── parser_service.py
│   │   ├── rag_service.py
│   │   ├── ai_service.py
│   │   ├── approval_service.py
│   │   └── document_service.py
│   │
│   ├── models/
│   │
│   ├── rag/
│   │   ├── embedding.py
│   │   ├── vector_store.py
│   │   ├── load_documents.py
│   │   ├── chunk_documents.py
│   │   ├── retriever.py
│   │   ├── rag_pipeline.py
│   │   └── build_vector_db.py
│   │
│   ├── chroma_db/
│   ├── data/
│   │   └── approvals.db
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    └── vite.config.js
```

---

## ☁️ Deployment

```
React + Vite → Netlify
FastAPI → Render (via Docker)
```

Docker packages Python, FastAPI, Tesseract OCR, Poppler, and all dependencies for a consistent backend environment.

### Environment Variables

```env
GEMINI_API_KEY=your_gemini_api_key
```

> 🔒 Never commit `.env` files or credentials to the repository.

---

## ⚠️ Error Handling

The backend gracefully handles:

- Invalid / unsupported files
- Empty PDFs
- OCR failures
- Text extraction failures
- No clauses detected
- Document not found
- Unexpected processing errors

---

## ✅ Testing

- **Document Processing:** Full pipeline tested from upload → AI analysis
- **API Testing:** Verified via FastAPI Swagger
- **Integration Testing:** Frontend ↔ Backend request/response flow
- **Deployment Testing:** Verified cloud communication between Netlify & Render

---

## 📈 Development Status

**Implemented:**
Legal Knowledge Base · PDF Upload & Validation · OCR · Parsing · Clause Extraction · RAG Pipeline · Gemini Embeddings · ChromaDB · LangChain · Gemini LLM · Risk Analysis · Recommendations · Human Approval Workflow · SQLite Persistence · Document Retrieval · FastAPI APIs · Swagger Docs · React Frontend · Frontend-Backend Integration · Docker · Cloud Deployment

**Current Status:** Functional end-to-end legal document intelligence workflow — from ingestion to AI analysis to human review to persistence.

---

## 🚀 Future Improvements

- Enterprise authentication & role-based access control
- Advanced document versioning
- Scalable database & vector database infrastructure
- Automated knowledge-base updates
- Advanced monitoring & logging
- Improved legal-domain evaluation & model benchmarking
- Multi-document analysis & comparison
- Enhanced audit logging & additional security controls

---

## 📌 Conclusion

Tata Legal AI demonstrates the practical application of **Generative AI and Retrieval-Augmented Generation** in the legal domain — taking a document from upload through extraction, clause identification, knowledge retrieval, AI analysis, risk assessment, human review, and final storage, while reducing repetitive manual review effort.

---

## ⚠️ Disclaimer

This project is developed for **demonstration, educational, and evaluation purposes** only.

AI-generated results should be reviewed by a **qualified legal professional** before being used for actual legal decisions. This system does **not** provide legal advice and does not replace professional legal judgment.

---

## 👥 Team Contributions — Team SkyAI-Squads

| # | Name | Contribution |
|---|------|---------------|
| 1 | **Hariom Upadhyay** | Team Leader / Group Representative — Product Testing & Solution, RAG, LangChain, Vector Database, LLM, Backend, Frontend, Deployment |
| 2 | Tanvi Rathore | Backend Handling, Backend-Frontend Integration, SQLite Database Handling |
| 3 | Poojitha Gaddam | OCR Handling |
| 4 | Mohmd Amaan Zaidi | Parsing |
| 5 | Prabhat Kumar Sasmal | Clause Extraction |
| 6 | Jyoti | RAG, LangChain and LLM Handling |
| 7 | Vishwajith Sonawane | Human Approval Handling |
| 8 | Suryansh | Frontend and Backend Deployment |
| 9 | Anas Khan | Frontend Handling |
| 10 | Shivaji, Vipul & Hitesh | Additional Project Contributions |

---

<p align="center">Made with ⚖️ + 🤖 by Team SkyAI-Squads</p>
