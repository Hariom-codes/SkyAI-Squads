# SkyAI-Legal — Integrated Legal Document Intelligence System

This package combines the React/Vite frontend and FastAPI backend into one authenticated workspace for the **SkyAI-Legal** team.

## What was added

- Secure login + account registration in the frontend.
- Passwords stored with Python `scrypt` hashing (not plaintext).
- Signed, expiring bearer sessions.
- Protected upload, approval, audit and knowledge-base APIs.
- Security response headers and a 15 MB PDF upload limit.
- Rotating backend application logs in `backend/data/logs/application.log`.
- SQLite audit logging for login, failed login, registration, upload, OCR, parsing, RAG, AI analysis and review decisions.
- Settings page with account/security status and Logout.
- Admin Panel with **SkyAI-Legal** team name and **Hariom Upadhyay** as group representative, plus registered-user list.
- Knowledge Base page containing the 30 supplied PDF knowledge-base documents, with each PDF available to open from the frontend.
- All visible `LegalIQ` branding has been replaced with **SkyAI-Legal**.

## Architecture

Frontend (React + Vite + Tailwind)
→ authenticated `POST /upload`
→ FastAPI
→ PDF OCR (Tesseract + Poppler)
→ Clause parser
→ SentenceTransformer embeddings
→ ChromaDB legal knowledge base
→ Gemini clause analysis
→ JSON results
→ Risk & Summary / Legal Review

## First-time setup on Windows

### 1. Backend

Open PowerShell in `backend`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `backend/.env` from `backend/.env.example` and set:

- `GOOGLE_API_KEY` — your Gemini API key.
- `AUTH_SECRET` — a long random secret. Change it before sharing/deployment.
- `ADMIN_PASSWORD` — change the demo admin password before deployment.

Do not commit or share the real `.env`.

Make sure Tesseract OCR and Poppler are installed and configured as required by the existing OCR service.

Run:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Or double-click `backend/run_backend.bat`.

Backend health: `http://127.0.0.1:8000/health`
Swagger: `http://127.0.0.1:8000/docs`

### 2. Frontend

Open a second PowerShell in `frontend`:

```powershell
npm install
npm run dev
```

Or double-click `frontend/run_frontend.bat`.

The frontend defaults to `http://127.0.0.1:8000`. To change it, create `frontend/.env` from `.env.example` and set `VITE_API_URL`.

## Login

Anyone can use **Create account** on the login screen to create a normal reviewer account.

The first backend startup creates the admin account using `ADMIN_USERNAME` and `ADMIN_PASSWORD` from `.env`. The default demo values are:

- Username: `hariom`
- Password: `SkyAI-Admin-2026!`

**Change the admin password and `AUTH_SECRET` before any public deployment.**

## Knowledge Base

The backend contains exactly 30 knowledge-base PDFs under:

`backend/data/Tata_Legal_Knowledge_Base_Complete_30_PDFs/`

The same 30 PDFs are also copied to:

`frontend/public/knowledge-base/`

The existing ChromaDB is included so the application can reuse the supplied vector store instead of rebuilding it at every startup.

## Logs and audit

- Application log: `backend/data/logs/application.log`
- Authentication users: `backend/data/security.db`
- Review + audit events: `backend/data/approvals.db`

For production use, add HTTPS, a real secret-management system, rate limiting/WAF, and a proper identity provider.
