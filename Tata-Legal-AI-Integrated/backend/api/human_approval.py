from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.approval_service import init_db, get_review, get_pending_reviews, save_review, get_audit_history
from api.auth import current_user_from_request

router = APIRouter()
init_db()

class ApprovalRequest(BaseModel):
    document_id: str
    reviewer: str = "legal_reviewer"
    comment: str = ""

class EditRequest(BaseModel):
    document_id: str
    reviewer: str = "legal_reviewer"
    edited_text: str
    comment: str = ""

@router.get("/approvals/pending")
async def pending_approvals(request: Request):
    current_user_from_request(request)
    return {"approvals": get_pending_reviews()}

@router.get("/approvals/{document_id}/{clause_id}")
async def get_approval(document_id: str, clause_id: str, request: Request):
    current_user_from_request(request)
    return get_review(document_id, clause_id)

@router.post("/approvals/{clause_id}/accept")
async def accept_approval(clause_id: str, request: ApprovalRequest, http_request: Request):
    user = current_user_from_request(http_request)
    return save_review(request.document_id, clause_id, "approved", user["display_name"], request.comment)

@router.post("/approvals/{clause_id}/reject")
async def reject_approval(clause_id: str, request: ApprovalRequest, http_request: Request):
    user = current_user_from_request(http_request)
    return save_review(request.document_id, clause_id, "rejected", user["display_name"], request.comment)

@router.put("/approvals/{clause_id}/edit")
async def edit_approval(clause_id: str, request: EditRequest, http_request: Request):
    user = current_user_from_request(http_request)
    return save_review(request.document_id, clause_id, "pending", user["display_name"], request.comment, request.edited_text)

@router.post("/approvals/{clause_id}/escalate")
async def escalate_approval(clause_id: str, request: ApprovalRequest, http_request: Request):
    user = current_user_from_request(http_request)
    return save_review(request.document_id, clause_id, "escalated", user["display_name"], request.comment)

@router.get("/audit")
async def audit(request: Request, document_id: str | None = None):
    current_user_from_request(request)
    return {"events": get_audit_history(document_id)}
