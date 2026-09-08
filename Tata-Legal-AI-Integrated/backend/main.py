import logging
import os
import time
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.auth import router as auth_router
from api.upload import router as upload_router
from api.human_approval import router as human_approval_router
from api.knowledge_base import router as knowledge_base_router
from services.auth_service import ensure_admin
from services.approval_service import init_db


# ============================================================
# BASE DIRECTORIES
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "data", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


# ============================================================
# LOGGING
# ============================================================

logger = logging.getLogger("skyai_legal")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, "application.log"),
        maxBytes=2_000_000,
        backupCount=5,
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# ============================================================
# DATABASE / ADMIN INITIALIZATION
# ============================================================

init_db()
ensure_admin()


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="SkyAI-Legal Backend",
    description="Secure legal document intelligence API",
    version="2.0.0",
)


# ============================================================
# CORS CONFIGURATION
# ============================================================

# Frontend development ports
default_origins = (
    "http://localhost:5173,"
    "http://localhost:5174,"
    "http://localhost:5175,"
    "http://localhost:5176,"
    "http://127.0.0.1:5173,"
    "http://127.0.0.1:5174,"
    "http://127.0.0.1:5175,"
    "http://127.0.0.1:5176"
)

origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        default_origins
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,

    # Allow all HTTP methods including CORS preflight OPTIONS
    allow_methods=["*"],

    # Allow Authorization, Content-Type and other frontend headers
    allow_headers=["*"],
)


# ============================================================
# SECURITY + REQUEST LOGGING MIDDLEWARE
# ============================================================

@app.middleware("http")
async def security_and_logging(request: Request, call_next):
    start = time.perf_counter()

    try:
        response = await call_next(request)

    except Exception:
        logger.exception(
            "Unhandled error | %s %s",
            request.method,
            request.url.path,
        )

        response = JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error."
            },
        )

    elapsed = round(
        (time.perf_counter() - start) * 1000,
        2,
    )

    # Security headers
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"

    # Prevent caching of authentication/upload responses
    if request.url.path.startswith(
        ("/auth", "/upload")
    ):
        response.headers["Cache-Control"] = "no-store"
    else:
        response.headers["Cache-Control"] = "no-cache"

    client_ip = (
        request.client.host
        if request.client
        else "unknown"
    )

    logger.info(
        "%s %s -> %s | %sms | ip=%s",
        request.method,
        request.url.path,
        response.status_code,
        elapsed,
        client_ip,
    )

    return response


# ============================================================
# API ROUTES
# ============================================================

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(human_approval_router)
app.include_router(knowledge_base_router)


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():
    return {
        "message": "SkyAI-Legal Backend is running",
        "team": "SkyAI-Legal",
        "version": app.version,
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "SkyAI-Legal Backend",
        "security": "enabled",
        "logging": "enabled",
    }