# SkyAI-Legal — Integrated Frontend

React + Vite + Tailwind frontend connected to the supplied FastAPI backend.

## Run

1. Start the backend first (see `../backend/README.md`).
2. In this folder:

```powershell
npm install
npm run dev
```

3. Open the Vite URL shown in the terminal.

The frontend sends PDFs to `POST http://127.0.0.1:8000/upload` by default.
To use another backend URL, create `.env` from `.env.example` and set `VITE_API_URL`.

## Connected features

- PDF upload to FastAPI `/upload`
- Real clause-level analysis results
- Risk level and confidence display
- RAG source display
- Executive summary display
- Human approval/reject/escalate calls
- Audit trail calls
- Dashboard populated from the latest analysis
