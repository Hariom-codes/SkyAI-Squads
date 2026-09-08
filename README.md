Tata Legal AI — Backend
Backend service for the Tata Legal AI Legal Document Intelligence System.

The backend is built with Python and FastAPI and provides the complete document-processing workflow: PDF validation, OCR-based text extraction, clause parsing, RAG-based legal knowledge retrieval, Gemini-based clause analysis, human approval workflow, and document-result persistence and retrieval.

1. Backend Overview
PDF Upload
    ↓
File Validation
    ↓
OCR / Text Extraction
    ↓
Clause Parsing
    ↓
RAG Retrieval
    ↓
ChromaDB Knowledge Base
    ↓
Google Gemini Analysis
    ↓
Risk Analysis + Recommendation
    ↓
Human Review / Approval
    ↓
Unique Document ID
    ↓
SQLite Result Persistence
    ↓
Document Result Retrieval
The backend exposes these capabilities through REST APIs and provides interactive API documentation through Swagger/OpenAPI.

2. Main Features
PDF upload and validation
OCR-based text extraction
Contract clause parsing
RAG-based legal knowledge retrieval
ChromaDB vector database integration
Sentence Transformers embeddings
Google Gemini clause analysis
Structured JSON AI output
Risk classification
Risk explanation
Recommendations
Retrieved source references
Human approval workflow
Unique document ID generation
Complete analysis-result persistence
Document-result retrieval using document_id
API health check
Swagger / OpenAPI documentation
Basic API error handling
3. Project Structure
backend/
│
├── api/
│   ├── upload.py
│   └── human_approval.py
│
├── services/
│   ├── ocr_service.py
│   ├── parser_service.py
│   ├── rag_service.py
│   ├── ai_service.py
│   ├── approval_service.py
│   └── document_service.py
│
├── models/
├── chroma_db/
├── data/
│   └── approvals.db
├── main.py
├── requirements.txt
├── requirements-full.txt
└── README.md
Local runtime/test files such as databases, vector-store data, backup files, and test PDFs should not be committed to Git unless explicitly required by the team.

4. Core Services
main.py
Creates the FastAPI application, configures CORS, and registers the API routers. It also provides the root and health-check endpoints.

api/upload.py
Contains the main document-processing API.

POST /upload connects the complete pipeline:

PDF → Validation → OCR → Clause Parsing → RAG → Gemini → Review → Persistence → JSON Response
It also provides:

GET /documents/{document_id}
for retrieving a previously stored document result.

services/ocr_service.py
Extracts text from uploaded PDF documents.

The current implementation uses:

pdf2image
PIL
pytesseract
PDF pages are converted into images and OCR is applied to extract text.

services/parser_service.py
Identifies and structures clauses from the extracted document text. The clauses are then processed individually by the RAG and AI services.

services/rag_service.py
Provides Retrieval-Augmented Generation support using:

Google Gemini
gemini-embedding-001
ChromaDB
Collection: tata_legal_knowledge
Relevant knowledge is retrieved for each clause and supplied as context to Gemini.

services/ai_service.py
Responsible for AI-based clause analysis.

The backend uses Google Gemini through the google-genai Python SDK.

Current model:

gemini-3.5-flash-lite
The AI receives the clause name, clause text, and retrieved legal context. It returns structured JSON containing fields such as:

Clause name
Summary
Risk level
Risk reason
Recommendation
The request is configured for an application/json response so the result can be consumed consistently by the backend and frontend.

services/approval_service.py
Handles human-review state for clauses, including statuses such as:

Pending
Approved
Rejected
Escalated
It also stores reviewer information, comments, and edited text where applicable.

api/human_approval.py
Exposes the human approval workflow through REST endpoints:

GET  /approvals/pending
GET  /approvals/{clause_id}

POST /approvals/{clause_id}/accept
POST /approvals/{clause_id}/reject
PUT  /approvals/{clause_id}/edit
POST /approvals/{clause_id}/escalate
services/document_service.py
Handles persistence and retrieval of complete document-analysis results using SQLite.

The documents table stores:

id
document_id
filename
result
created_at
The complete analysis result is stored as JSON.

5. RAG Configuration
Embedding model:

gemini-embedding-001
Vector database:

ChromaDB
Collection:

tata_legal_knowledge
The prototype uses a local ChromaDB knowledge base. Knowledge-base materials should be maintained according to the team's agreed reference materials and access classification.

6. Gemini AI Configuration
The backend uses Google Gemini through the google-genai Python SDK.

Current model:

gemini-3.5-flash-lite
Required environment variable:

GEMINI_API_KEY=your_gemini_api_key
The API key must remain private and must never be committed to GitHub.

7. Human Approval Workflow
AI-generated analysis is not automatically treated as final approved legal work.

A reviewer can:

View pending clauses
Accept an analysis
Reject an analysis
Edit the reviewed text
Escalate a clause for further review
This provides a human-in-the-loop workflow around the AI-generated analysis.

8. Document Result Persistence
After a PDF is successfully processed, the backend generates a unique document ID using UUID.

Example:

DOC-9C085A8A7B7B
The complete result is then stored in SQLite together with:

document_id
Filename
Complete analysis result
Creation timestamp
This allows the analysis to remain available after the original upload request has finished.

9. Document Result Retrieval
Endpoint:

GET /documents/{document_id}
Example:

GET /documents/DOC-9C085A8A7B7B
The endpoint searches SQLite using the document ID and returns the previously saved result.

If the document ID does not exist, the API returns:

HTTP 404
Document not found.
This allows the frontend to retrieve an earlier analysis without uploading and processing the same PDF again.

10. API Endpoints
Basic
GET /
GET /health
Document Processing
POST /upload
GET /documents/{document_id}
Human Approval
GET  /approvals/pending
GET  /approvals/{clause_id}
POST /approvals/{clause_id}/accept
POST /approvals/{clause_id}/reject
PUT  /approvals/{clause_id}/edit
POST /approvals/{clause_id}/escalate
11. Swagger / OpenAPI Documentation
FastAPI automatically provides interactive API documentation.

After starting the backend, open:

http://localhost:8000/docs
Swagger can be used to:

View available endpoints
Upload a test PDF
Execute API requests
Inspect JSON responses
Test approval operations
Test document-result retrieval
A typical persistence test is:

POST /upload
      ↓
Receive document_id
      ↓
GET /documents/{document_id}
      ↓
Verify the saved analysis result
12. Upload API
Endpoint:

POST /upload
The backend:

Validates the uploaded file.
Verifies that it is a PDF.
Checks that it is not empty.
Extracts text using OCR.
Parses the extracted text into clauses.
Retrieves relevant legal knowledge using RAG.
Analyzes each clause using Gemini.
Attaches retrieved source information.
Adds human-review information.
Generates a unique document_id.
Persists the complete result in SQLite.
Returns the structured JSON response.
13. Analysis Response
Each analyzed clause can contain:

clause_no
clause_name
clause_text
clause_id
analysis
sources
human_review
The AI analysis contains:

clause_name
summary
risk_level
risk_reason
recommendation
Retrieved sources can contain:

source
page
14. Error Handling
Examples:

Non-PDF file

HTTP 400
Only PDF files are supported.
Empty PDF

HTTP 400
The uploaded PDF is empty.
Unable to extract text

HTTP 422
Could not extract text from the PDF.
No clauses detected

HTTP 422
No clauses could be identified in the document.
Missing document ID

HTTP 404
Document not found.
Unexpected processing error

HTTP 500
An error occurred while processing the document.
The AI analysis also has exception handling so that an individual clause-analysis failure can return a fallback response instead of unnecessarily terminating the complete document-processing flow.

15. Environment Setup
Create a .env file inside the backend directory:

GEMINI_API_KEY=your_gemini_api_key
If Poppler is not available through the system PATH, configure the Poppler Library\bin path according to the local machine/environment.

Do not commit .env or API keys to GitHub.

16. Installation
From the backend directory:

python -m venv venv
Activate the virtual environment:

..�env\Scripts\Activate.ps1
Install dependencies:

pip install -r requirements.txt
17. Run the Backend
From the backend directory:

python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
Local backend:

http://localhost:8000
Swagger:

http://localhost:8000/docs
18. Backend Testing
The backend was tested through FastAPI Swagger.

The document persistence flow was verified by:

POST /upload
      ↓
PDF processed successfully
      ↓
Unique document_id generated
      ↓
Complete result stored
      ↓
GET /documents/{document_id}
      ↓
Previously saved result returned
This verifies the document-result persistence and retrieval workflow.

🚀 Deployment
The Tata Legal AI Document Intelligence System is deployed using a modern cloud-based architecture.

Frontend
Platform: Netlify
Technology: React + Vite
The frontend provides the user interface for PDF upload, document analysis, risk assessment, clause extraction, and AI-generated results.
Backend
Platform: Render
Technology: FastAPI + Python
The backend exposes REST APIs for document processing, OCR, RAG retrieval, and AI analysis.
Containerization
Docker is used to package the backend and its system dependencies.
Tesseract OCR is installed inside the Docker container for scanned/image-based PDF processing.
Poppler is used for PDF-to-image conversion during OCR processing.
AI & RAG
Google Gemini API is used for LLM-based analysis.
Gemini Embedding (gemini-embedding-001) is used for semantic embeddings.
ChromaDB is used as the vector database for storing and retrieving relevant legal document chunks.
LangChain is used to implement the RAG workflow.
Deployment Flow
Frontend (Netlify) ↓ FastAPI Backend (Render) ↓ Docker Container ↓ PDF Processing + OCR ↓ RAG Retrieval using ChromaDB ↓ Gemini LLM ↓ Legal Analysis & Risk Assessment ↓ Results displayed on Frontend

19. Development Status
Core Backend
PDF upload and validation — Complete
OCR-based text extraction — Complete
Clause parsing — Complete
RAG retrieval — Complete
ChromaDB integration — Complete
Gemini AI analysis — Complete
Structured JSON AI output — Complete
Risk analysis and recommendations — Complete
Human approval workflow — Complete
Unique document ID generation — Complete
Complete analysis-result persistence — Complete
Document-result retrieval — Complete
FastAPI REST API — Complete
Swagger / OpenAPI documentation — Complete
Basic API error handling — Complete
Production Readiness
The core end-to-end workflow is functional.

Additional production-oriented improvements can include enterprise authentication and authorization, scalable database/storage infrastructure, environment-based OCR configuration, automated knowledge-base provisioning, monitoring, logging, rate limiting, and deployment hardening.

20. Important Disclaimer
This project is an AI-assisted legal document intelligence system developed for demonstration and evaluation purposes.

The system is designed to support legal and compliance professionals by assisting with document processing, clause analysis, risk identification, retrieval of relevant knowledge, and review workflows.

AI-generated outputs are intended to support human decision-making and must be reviewed by a qualified legal professional before being treated as an approved legal work product. The system does not provide legal advice or replace professional legal judgment.

Knowledge-base materials used in the demonstration should be interpreted according to their stated provenance and access classification and should not be represented as confidential Tata legal positions unless explicitly authorized.

21. Team / Frontend Integration
The backend provides structured JSON responses that the frontend can consume to display:

Contract information
Extracted clauses
Clause summaries
Risk levels
Risk reasons
Recommendations
Retrieved source references
Human-review information
Document IDs
The frontend can use:

POST /upload
to process a document and receive its document_id.

It can later use:

GET /documents/{document_id}
to retrieve the stored result.

The backend is designed to work with the team's current frontend upload and review flow.

22. Backend Architecture
                    Frontend
                       │
                       │ REST API
                       ▼
                    FastAPI
                       │
                   /upload
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    OCR Service   Parser Service   Approval Service
        │              │
        └──────────────┤
                       ▼
                  RAG Service
                       │
                       ▼
                    ChromaDB
                       │
                Retrieved Context
                       │
                       ▼
                  Gemini AI
                       │
                       ▼
                Clause Analysis
                       │
                       ▼
              Document Service
                       │
                       ▼
                  SQLite DB
                       │
                       ▼
          /documents/{document_id}
                       │
                       ▼
                    Frontend
23. Project Status
Current Status: Functional End-to-End Backend Implementation

The core document intelligence, AI analysis, human review, persistence, and retrieval workflow is implemented and testable through the backend API.

The backend is ready for frontend integration and can be further hardened for production deployment as required.

24. Team Contribution
Hariom Upadhyay : Team Leader/Group Representative, Product Testing & Solution, RAG & LangChain & Vector Database, LLM, Backend, Frontend, Deployment


Tanvi Rathore : Backend Handling, Backend-Frontend Integration, SQLite Database Handling


Poojitha Gaddam : OCR Handling


Mohmd Amaan Zaidi : Parsing


Prabhat Kumar Sasmal : Clause Extraction


Jyoti : RAG & LangChain & LLM Handling


Vishwajith Sonawane : Human Approval Handling


🏁 Project Conclusion
The Tata Legal AI Document Intelligence System provides an AI-powered solution for simplifying and accelerating legal document analysis. It combines OCR, PDF parsing, clause extraction, Retrieval-Augmented Generation (RAG), LangChain, vector search, and Large Language Models (LLMs) to process complex legal documents and generate meaningful insights.

The system helps identify important clauses, retrieve relevant legal knowledge, assess potential risks, and present the results through an easy-to-use interface. The integration of Gemini, ChromaDB, and modern cloud deployment technologies makes the solution practical and scalable.

Overall, the project demonstrates how Generative AI and RAG can be applied to the legal domain to reduce manual effort, improve information retrieval, and support faster and more structure.
