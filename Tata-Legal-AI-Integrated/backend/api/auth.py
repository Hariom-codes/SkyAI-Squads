from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from services.auth_service import authenticate, create_user, ensure_admin, issue_token, verify_token, list_users, security_summary
from services.approval_service import add_audit_event

router = APIRouter(prefix="/auth", tags=["Authentication"])
ensure_admin()


class LoginRequest(BaseModel):
    username: str = Field(min_length=3, max_length=80)
    password: str = Field(min_length=1, max_length=200)


class RegisterRequest(BaseModel):
    username: str = Field(min_length=3, max_length=80)
    password: str = Field(min_length=8, max_length=200)
    display_name: str = Field(min_length=1, max_length=120)


def current_user_from_request(request: Request):
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication required.")
    user = verify_token(auth[7:].strip())
    if not user:
        raise HTTPException(status_code=401, detail="Session expired or invalid. Please log in again.")
    return user


def require_admin(request: Request):
    user = current_user_from_request(request)
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Administrator access required.")
    return user


@router.post("/login")
def login(body: LoginRequest, request: Request):
    user = authenticate(body.username, body.password)
    if not user:
        add_audit_event("AUTH", "Login Failed", f"Failed login for username {body.username.strip().lower()}", body.username.strip().lower(), "Authentication", "Failed")
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    token = issue_token(user)
    add_audit_event("AUTH", "Login", f"{user['username']} logged in", user["display_name"], user["role"], "Completed")
    return {"token": token, "user": user}


@router.post("/register")
def register(body: RegisterRequest):
    try:
        user = create_user(body.username, body.password, body.display_name, "reviewer")
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    add_audit_event("AUTH", "User Registered", f"New account {user['username']} created", user["display_name"], "Reviewer", "Completed")
    return {"message": "Account created successfully. You can now log in.", "user": user}


@router.get("/me")
def me(request: Request):
    user = current_user_from_request(request)
    return {"user": user}


@router.get("/security")
def security(request: Request):
    user = current_user_from_request(request)
    return {"user": user, **security_summary()}


@router.get("/users")
def users(request: Request):
    require_admin(request)
    return {"users": list_users()}
