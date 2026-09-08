#  Tata Group: AI Legal Document Intelligence System

## Project Overview

Tata Legal AI — Legal Document Intelligence System is an AI-powered solution developed by **Team SkyAI-Squads** which led by Hariom Upadhyay(Group Representative) to simplify and accelerate the analysis of legal documents.

The system is designed to process legal PDF documents and automatically extract useful information such as clauses, summaries, potential risks, supporting legal knowledge, and recommendations.

The project combines PDF processing, OCR, text parsing, clause extraction, Retrieval-Augmented Generation (RAG), LangChain, Gemini Embeddings, ChromaDB, Google Gemini LLM, SQLite database, FastAPI, React, Docker, and cloud deployment into a single end-to-end legal document intelligence platform.

The complete workflow starts from document upload and continues through document processing, clause extraction, knowledge retrieval, AI analysis, risk assessment, human review, and result storage.

## Objective

The primary objective of the project is to reduce the manual effort involved in reviewing lengthy legal documents.

Instead of manually reviewing every page and clause, the system helps users:

- Upload legal documents
- Extract text from PDF documents
- Process scanned documents using OCR
- Parse and structure document content
- Identify important legal clauses
- Retrieve relevant legal knowledge
- Analyze clauses using Generative AI
- Identify potential risks
- Generate explanations and recommendations
- Review AI-generated results through human approval
- Store processed document results
- Retrieve previously processed documents using a unique document ID

The system is designed as an AI-assisted solution where human review remains an important part of the overall workflow.

### 🔗 Live Links

- **Frontend:** https://eclectic-biscotti-bca046.netlify.app/
- **Backend:** https://skyai-squads-aco3.onrender.com/
- **GitHub Repository:** https://github.com/Hariom-codes/SkyAI-Squads

## Legal Knowledge Base

The project uses a dedicated legal knowledge base containing **30 PDF documents**.

These documents provide reference knowledge that is used by the RAG system during legal clause analysis.

### Knowledge Base Workflow

```text
30 Legal PDF Documents
        |
        v
Document Loading
        |
        v
Text Extraction
        |
        v
Text Chunking
        |
        v
Gemini Embeddings
        |
        v
ChromaDB
        |
        v
Semantic Search
        |
        v
Relevant Legal Knowledge
        |
        v
Gemini LLM



## Backend

Backend service for the Tata Legal AI Legal Document Intelligence System.

The backend is built with Python and FastAPI and provides the complete document-processing workflow: PDF validation, OCR-based text extraction, clause parsing, RAG-based legal knowledge retrieval, Gemini-based clause analysis, human approval workflow, and document-result persistence and retrieval.

1. Backend Overview
PDF Upload
    |
    v
File Validation
    |
    v
OCR / Text Extraction
    |
    v
Clause Parsing
    |
    v
RAG Retrieval
    |
    v
ChromaDB Knowledge Base
    |
    v
Google Gemini Analysis
    |
    v
Risk Analysis + Recommendation
    |
    v
Human Review / Approval
    |
    v
Unique Document ID
    |
    v
SQLite Result Persistence
    |
    v
Document Result Retrieval

The backend exposes these capabilities through REST APIs and provides interactive API documentation through Swagger/OpenAPI.


## 2. Main Features

- PDF upload and validation
- OCR-based text extraction
- Contract clause parsing
- RAG-based legal knowledge retrieval
- ChromaDB vector database integration
- Sentence Transformers embeddings
- Google Gemini clause analysis
- Structured JSON AI output
- Risk classification
- Risk explanation
- Recommendations
- Retrieved source references
- Human approval workflow
- Unique document ID generation
- Complete analysis-result persistence
- Document-result retrieval using `document_id`
- API health check
- Swagger / OpenAPI documentation
- Basic API error handling

---

## 3. Project Structure

```text
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
```

> Local runtime/test files such as databases, vector-store data, backup files, and test PDFs should not be committed to Git unless explicitly required by the team.

---

## 4. Core Services

### `main.py`

Creates the FastAPI application, configures CORS, and registers the API routers. It also provides the root and health-check endpoints.

### `api/upload.py`

Contains the main document-processing API.

`POST /upload` connects the complete pipeline:

```text
PDF → Validation → OCR → Clause Parsing → RAG → Gemini → Review → Persistence → JSON Response
```

It also provides:

```text
GET /documents/{document_id}
```

for retrieving a previously stored document result.

### `services/ocr_service.py`

Extracts text from uploaded PDF documents.

The current implementation uses:

- `pdf2image`
- `PIL`
- `pytesseract`

PDF pages are converted into images and OCR is applied to extract text.

### `services/parser_service.py`

Identifies and structures clauses from the extracted document text. The clauses are then processed individually by the RAG and AI services.

### `services/rag_service.py`

Provides Retrieval-Augmented Generation support using:

- Sentence Transformers
- `all-MiniLM-L6-v2`
- ChromaDB
- Collection: `tata_legal_knowledge`

Relevant knowledge is retrieved for each clause and supplied as context to Gemini.

### `services/ai_service.py`

Responsible for AI-based clause analysis.

The backend uses **Google Gemini** through the `google-genai` Python SDK.

Current model:

```text
gemini-3.5-flash-lite
```

The AI receives the clause name, clause text, and retrieved legal context. It returns structured JSON containing fields such as:

- Clause name
- Summary
- Risk level
- Risk reason
- Recommendation

The request is configured for an `application/json` response so the result can be consumed consistently by the backend and frontend.

### `services/approval_service.py`

Handles human-review state for clauses, including statuses such as:

- Pending
- Approved
- Rejected
- Escalated

It also stores reviewer information, comments, and edited text where applicable.

### `api/human_approval.py`

Exposes the human approval workflow through REST endpoints:

```text
GET  /approvals/pending
GET  /approvals/{clause_id}

POST /approvals/{clause_id}/accept
POST /approvals/{clause_id}/reject
PUT  /approvals/{clause_id}/edit
POST /approvals/{clause_id}/escalate
```

### `services/document_service.py`

Handles persistence and retrieval of complete document-analysis results using SQLite.

The `documents` table stores:

```text
id
document_id
filename
result
created_at
```

The complete analysis result is stored as JSON.

---

## 5. RAG Configuration

## RAG and LangChain Implementation

The RAG (Retrieval-Augmented Generation) module is responsible for connecting the legal knowledge base with the Generative AI analysis pipeline.

The purpose of the RAG system is to retrieve relevant legal information from the stored knowledge base and provide it as contextual information to the Gemini LLM during document analysis.

### RAG Pipeline

```text
Legal PDF Knowledge Base
        |
        v
PDF Document Loading
        |
        v
Text Extraction
        |
        v
Document Chunking
        |
        v
Gemini Embeddings
(gemini-embedding-001)
        |
        v
ChromaDB Vector Database
        |
        v
Semantic Retrieval
        |
        v
Top Relevant Legal Chunks
        |
        v
Gemini LLM
        |
        v
Risk Analysis and Recommendation

RAG Components

The RAG implementation is organized inside the backend/rag directory.

Document Loading

Legal reference PDFs are loaded from the knowledge-base directory using the PDF document loader.

Each document is processed along with metadata such as its source and page information.

Document Chunking

Large legal documents are divided into smaller text chunks before creating embeddings.

The project uses LangChain's RecursiveCharacterTextSplitter with:

Chunk size: 1200
Chunk overlap: 150

The overlap helps preserve context between neighboring chunks.

Gemini Embeddings

The project uses Google's Gemini embedding model:

gemini-embedding-001

The generated embeddings use a dimensionality of:

768

Two retrieval-oriented task types are used:

RETRIEVAL_DOCUMENT for knowledge-base documents
RETRIEVAL_QUERY for user/document queries

The Gemini embedding implementation follows LangChain's Embeddings interface so that it can work directly with the ChromaDB vector store.

ChromaDB

The generated embeddings are stored in ChromaDB.

ChromaDB acts as the vector database for the legal knowledge base and allows the system to perform semantic similarity searches.

The vector database stores:

Document chunks
Embeddings
Source metadata
Page information
Semantic Retrieval

When a clause or query needs legal context, the query is converted into an embedding and searched against the ChromaDB knowledge base.

The retriever is configured to return the top 3 relevant documents.

This allows the system to provide the Gemini LLM with the most relevant legal knowledge instead of processing the entire knowledge base.

LangChain Integration

LangChain is used as the framework for connecting different components of the RAG pipeline.

The RAG implementation uses LangChain for:

Embedding interface
Document processing
Text splitting
ChromaDB integration
Vector retrieval
RAG pipeline integration

The overall LangChain flow is:

Documents
    |
    v
LangChain Document Processing
    |
    v
Recursive Character Text Splitter
    |
    v
Gemini Embeddings
    |
    v
ChromaDB
    |
    v
LangChain Retriever
    |
    v
Relevant Context
    |
    v
Gemini LLM

RAG Files

The main RAG-related files are:

backend/
|
+-- rag/
|   |
|   +-- embedding.py
|   +-- load_documents.py
|   +-- chunk_documents.py
|   +-- vector_store.py
|   +-- retriever.py
|   +-- rag_pipeline.py
|   +-- build_vector_db.py
|
+-- services/
    |
    +-- rag_service.py
File Responsibilities
embedding.py

Implements the Gemini embedding model using:

gemini-embedding-001

It provides document and query embeddings through the LangChain Embeddings interface.

load_documents.py

Loads the legal PDF documents and prepares them for processing.

It also preserves document metadata such as source and page information.

chunk_documents.py

Splits extracted legal text into smaller chunks using LangChain's RecursiveCharacterTextSplitter.

Configuration:

chunk_size = 1200
chunk_overlap = 150
vector_store.py

Initializes and connects the application to ChromaDB.

The Gemini embedding function is used to create and search vector representations of the legal knowledge.

retriever.py

Creates the ChromaDB retriever and retrieves the most relevant legal knowledge for a given query.

The retriever returns the top 3 relevant chunks.

rag_pipeline.py

Coordinates the process of loading legal documents, chunking them, generating embeddings, and storing them in ChromaDB.

build_vector_db.py

Provides the entry point for building the legal knowledge vector database.

rag_service.py

Acts as the service layer between the FastAPI backend and the RAG retrieval system.

It receives a query, retrieves relevant legal documents, and returns the retrieved content along with source and page metadata.

RAG to LLM Flow

The complete process during document analysis is:

Uploaded Legal Document
        |
        v
Clause Extraction
        |
        v
Clause / Query
        |
        v
Gemini Query Embedding
        |
        v
ChromaDB Semantic Search
        |
        v
Top 3 Relevant Legal Chunks
        |
        v
Retrieved Legal Context
        |
        v
Gemini LLM
        |
        v
Risk Assessment
        |
        v
Recommendation

Why RAG is Used

A legal document analysis system should not rely only on the general knowledge of an LLM.

RAG allows the system to retrieve relevant information from the project's own legal knowledge base before generating an answer.

This provides the model with additional domain-specific context and helps make the generated analysis more relevant to the legal documents being processed.

My Contribution

The RAG and LangChain component covers the implementation and integration of:

RAG pipeline
LangChain document processing
Text chunking
Gemini embeddings
ChromaDB vector database
Semantic retrieval
Retriever configuration
RAG service integration
Retrieved-context flow to the Gemini LLM

## LLM Integration

The Large Language Model (LLM) is responsible for analyzing the uploaded legal document and generating meaningful legal insights based on the extracted clauses and the relevant context retrieved from the RAG pipeline.

The project uses **Google Gemini** as the Generative AI model.

### LLM Workflow

```text
Uploaded Legal Document
        |
        v
Text Extraction
        |
        v
Clause Extraction
        |
        v
Clause / Legal Query
        |
        v
RAG Retrieval
        |
        v
Relevant Legal Context
        |
        v
Gemini LLM
        |
        v
Clause Analysis
        |
        v
Risk Assessment
        |
        v
Recommendation

Role of the LLM

The Gemini LLM processes the extracted legal clauses together with the relevant legal knowledge retrieved from ChromaDB.

The LLM is responsible for:

Analyzing legal clauses
Understanding clause meaning and context
Identifying potential legal risks
Classifying the level of risk
Providing reasoning for the identified risk
Generating recommendations
Supporting the human review and approval workflow
RAG + LLM Integration

The LLM does not work in isolation.

The RAG pipeline first retrieves relevant legal knowledge from the ChromaDB knowledge base. This retrieved information is then provided as contextual input to the Gemini LLM.

User / Uploaded Document
        |
        v
Clause Extraction
        |
        v
RAG Query
        |
        v
Gemini Embedding
        |
        v
ChromaDB Semantic Search
        |
        v
Relevant Legal Context
        |
        v
Prompt Construction
        |
        v
Gemini LLM
        |
        v
AI Legal Analysis

Gemini Model

The project uses the Gemini model configured through the environment variable:

GEMINI_MODEL

The current project configuration uses:

gemini-3.5-flash-lite

The API key is loaded through the environment variable:

GEMINI_API_KEY

The API key is not stored directly in the source code or committed to the GitHub repository.

Prompt-Based Analysis

The retrieved legal context and extracted clause are combined into the input provided to the Gemini LLM.

The analysis flow can be represented as:

Legal Clause
     +
Retrieved Legal Knowledge
     +
Analysis Instructions
     |
     v
Gemini LLM
     |
     v
Risk Analysis
     +
Reasoning
     +
Recommendation

This allows the generated analysis to use both the uploaded document and the project's legal knowledge base.

Risk Analysis

The LLM evaluates the clause and generates a risk assessment based on the available legal context.

The analysis can identify potential issues such as:

Unfavorable contractual terms
Ambiguous clauses
Compliance-related concerns
Financial or commercial risks
Legal obligations
Missing or potentially problematic conditions
Recommendation Generation

After identifying potential risks, the LLM generates recommendations that can help a reviewer understand what should be examined or improved in the clause.

The recommendations are presented as part of the document analysis results and can be reviewed through the human approval workflow.

LLM Contribution

The LLM component integrates:

Google Gemini
Prompt-based legal clause analysis
RAG-retrieved context
Risk assessment
Legal recommendations
Human-in-the-loop review

The combination of RAG + LangChain + ChromaDB + Gemini LLM forms the core Generative AI pipeline of the legal document intelligence system.


## 7. Human Approval Workflow

The LLM-generated analysis is not treated as a final legal decision.

The system includes a human review and approval workflow where the generated results can be reviewed before being finalized.Gemini LLM
    |
    v
AI-Generated Analysis
    |
    v
Human Review
    |
    +----> Approve
    |
    +----> Reject
    |
    +----> Edit
    |
    +----> Escalate


## 8. Document Result Persistence

After a PDF is successfully processed, the backend generates a unique document ID using UUID.

Example:

```text
DOC-9C085A8A7B7B
```

The complete result is then stored in SQLite together with:

- `document_id`
- Filename
- Complete analysis result
- Creation timestamp

This allows the analysis to remain available after the original upload request has finished.

---

## 9. Document Result Retrieval

**Endpoint:**

```text
GET /documents/{document_id}
```

Example:

```text
GET /documents/DOC-9C085A8A7B7B
```

The endpoint searches SQLite using the document ID and returns the previously saved result.

If the document ID does not exist, the API returns:

```text
HTTP 404
Document not found.
```

This allows the frontend to retrieve an earlier analysis without uploading and processing the same PDF again.

---

## 10. API Endpoints

### Basic

```text
GET /
GET /health
```

### Document Processing

```text
POST /upload
GET /documents/{document_id}
```

### Human Approval

```text
GET  /approvals/pending
GET  /approvals/{clause_id}
POST /approvals/{clause_id}/accept
POST /approvals/{clause_id}/reject
PUT  /approvals/{clause_id}/edit
POST /approvals/{clause_id}/escalate
```

---

## 11. Swagger / OpenAPI Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

```text
http://localhost:8000/docs
```

Swagger can be used to:

- View available endpoints
- Upload a test PDF
- Execute API requests
- Inspect JSON responses
- Test approval operations
- Test document-result retrieval

A typical persistence test is:

```text
POST /upload
      ↓
Receive document_id
      ↓
GET /documents/{document_id}
      ↓
Verify the saved analysis result
```

---

## 12. Upload API

**Endpoint:**

```text
POST /upload
```

The backend:

1. Validates the uploaded file.
2. Verifies that it is a PDF.
3. Checks that it is not empty.
4. Extracts text using OCR.
5. Parses the extracted text into clauses.
6. Retrieves relevant legal knowledge using RAG.
7. Analyzes each clause using Gemini.
8. Attaches retrieved source information.
9. Adds human-review information.
10. Generates a unique `document_id`.
11. Persists the complete result in SQLite.
12. Returns the structured JSON response.

---

## 13. Analysis Response

Each analyzed clause can contain:

```text
clause_no
clause_name
clause_text
clause_id
analysis
sources
human_review
```

The AI analysis contains:

```text
clause_name
summary
risk_level
risk_reason
recommendation
```

Retrieved sources can contain:

```text
source
page
```

---

## 14. Error Handling

Examples:

**Non-PDF file**

```text
HTTP 400
Only PDF files are supported.
```

**Empty PDF**

```text
HTTP 400
The uploaded PDF is empty.
```

**Unable to extract text**

```text
HTTP 422
Could not extract text from the PDF.
```

**No clauses detected**

```text
HTTP 422
No clauses could be identified in the document.
```

**Missing document ID**

```text
HTTP 404
Document not found.
```

**Unexpected processing error**

```text
HTTP 500
An error occurred while processing the document.
```

The AI analysis also has exception handling so that an individual clause-analysis failure can return a fallback response instead of unnecessarily terminating the complete document-processing flow.

---

## 15. Environment Setup

Create a `.env` file inside the backend directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

If Poppler is not available through the system PATH, configure the Poppler `Library\bin` path according to the local machine/environment.

Do not commit `.env` or API keys to GitHub.

---

## 16. Installation

From the backend directory:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
..env\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## 17. Run the Backend

From the `backend` directory:

```powershell
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Local backend:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## 18. Backend Testing

The backend was tested through FastAPI Swagger.

The document persistence flow was verified by:

```text
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
```

This verifies the document-result persistence and retrieval workflow.

---

## 19. Development Status

### Core Backend

- PDF upload and validation — Complete
- OCR-based text extraction — Complete
- Clause parsing — Complete
- RAG retrieval — Complete
- ChromaDB integration — Complete
- Gemini AI analysis — Complete
- Structured JSON AI output — Complete
- Risk analysis and recommendations — Complete
- Human approval workflow — Complete
- Unique document ID generation — Complete
- Complete analysis-result persistence — Complete
- Document-result retrieval — Complete
- FastAPI REST API — Complete
- Swagger / OpenAPI documentation — Complete
- Basic API error handling — Complete

### Production Readiness

The core end-to-end workflow is functional.

Additional production-oriented improvements can include enterprise authentication and authorization, scalable database/storage infrastructure, environment-based OCR configuration, automated knowledge-base provisioning, monitoring, logging, rate limiting, and deployment hardening.

---

## 20. Important Disclaimer

This project is an **AI-assisted legal document intelligence system developed for demonstration and evaluation purposes**.

The system is designed to support legal and compliance professionals by assisting with document processing, clause analysis, risk identification, retrieval of relevant knowledge, and review workflows.

AI-generated outputs are intended to support human decision-making and must be reviewed by a qualified legal professional before being treated as an approved legal work product. The system does not provide legal advice or replace professional legal judgment.

Knowledge-base materials used in the demonstration should be interpreted according to their stated provenance and access classification and should not be represented as confidential Tata legal positions unless explicitly authorized.

---

## 21. Team / Frontend Integration

The backend provides structured JSON responses that the frontend can consume to display:

- Contract information
- Extracted clauses
- Clause summaries
- Risk levels
- Risk reasons
- Recommendations
- Retrieved source references
- Human-review information
- Document IDs

The frontend can use:

```text
POST /upload
```

to process a document and receive its `document_id`.

It can later use:

```text
GET /documents/{document_id}
```

to retrieve the stored result.

The backend is designed to work with the team's current frontend upload and review flow.

---

## 22. Backend Architecture

```text
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
```

---

## 23. Project Status

**Current Status: Functional End-to-End Backend Implementation**

The core document intelligence, AI analysis, human review, persistence, and retrieval workflow is implemented and testable through the backend API.

The backend is ready for frontend integration and can be further hardened for production deployment as required.


## Frontend

The frontend of the Tata Legal AI — Legal Document Intelligence System is developed using React and Vite.

It provides the complete user-facing interface through which users can upload legal PDF documents, interact with the system, and view AI-generated legal analysis in a structured format.

### Frontend Technologies

The frontend is built using:

- React
- Vite
- JavaScript
- HTML
- CSS
- REST API integration

### Frontend Responsibilities

The frontend handles the complete user interaction layer of the application.

It provides functionality for:

- Uploading legal PDF documents
- Sending documents to the FastAPI backend
- Displaying document-processing results
- Displaying extracted clauses
- Displaying clause summaries
- Displaying risk levels
- Displaying risk reasons
- Displaying AI-generated recommendations
- Displaying analysis results
- Supporting the human review workflow
- Communicating with the backend through REST APIs

### Frontend Application Flow

The frontend follows a request-and-response architecture.

```text
User
 |
 v
React Frontend
 |
 v
PDF Upload
 |
 v
API Request
 |
 v
FastAPI Backend
 |
 v
Document Processing
 |
 v
OCR / Text Extraction
 |
 v
Parsing
 |
 v
Clause Extraction
 |
 v
RAG Retrieval
 |
 v
Gemini AI Analysis
 |
 v
JSON Response
 |
 v
React Frontend
 |
 v
Analysis Results

Document Upload

The user can select a legal PDF document from the frontend and submit it for analysis.

The selected document is sent to the FastAPI backend through the /upload endpoint.

PDF File
   |
   v
React Upload Interface
   |
   v
FormData
   |
   v
POST /upload
   |
   v
FastAPI Backend

After processing is completed, the backend returns the analysis result to the frontend.

Frontend-Backend Integration

The frontend communicates with the FastAPI backend using HTTP REST APIs.

The backend URL is configured through the Vite environment variable:

VITE_API_BASE_URL

This allows the frontend to communicate with different backend environments, including local development and the deployed Render backend.

The integration flow is:

React Frontend
      |
      v
API Client
      |
      v
FastAPI REST API
      |
      v
Backend Processing
      |
      v
JSON Response
      |
      v
React Frontend
      |
      v
Results Display

API Client

The frontend uses a centralized API client for communication with the backend.

The API client handles:

API requests
Request headers
JSON responses
FormData requests
Authentication token handling
Request timeout
Backend error handling
Backend connection errors

For document upload, the selected PDF is sent to the backend using FormData.

The primary document-processing request is:

POST /upload

Document Service

The frontend contains a document service for handling document-related operations.

The document service handles:

Document upload
Document retrieval
Storing the latest analysis result
Storing the current document ID
Communication with the backend API

The document upload flow is:

User Selects PDF
      |
      v
documentService
      |
      v
FormData
      |
      v
API Client
      |
      v
POST /upload
      |
      v
FastAPI Backend
      |
      v
Analysis Result
      |
      v
React Frontend

Result Display

After the backend completes the document-processing pipeline, the frontend receives a structured JSON response.

The frontend displays information such as:

Document information
Extracted clauses
Clause summaries
Risk levels
Risk explanations
Recommendations
AI-generated analysis

The results are presented in a structured interface so that users can understand the analysis more easily.

Human Approval Interface

The frontend supports the Human-in-the-Loop review workflow.

AI-generated results can be reviewed by a human before the final action is taken.

The review flow is:

AI Generated Analysis
        |
        v
Human Review
        |
   +----+----+----+
   |         |    |
   v         v    v
Approve    Reject Escalate
   |
   v
Updated Result

The frontend communicates the review actions to the corresponding backend APIs.

The supported review actions include:

Approve
Reject
Edit
Escalate
Session-Based Result Handling

The frontend uses browser session storage to maintain the current document context during the user session.

The application stores:

Latest analysis result
Current document ID

This allows the frontend to maintain the latest processed document and its analysis while the user interacts with the application.

Frontend Project Structure

frontend/
|
├── src/
|   |
|   ├── components/
|   ├── data/
|   ├── hooks/
|   ├── i18n/
|   ├── layouts/
|   ├── pages/
|   |
|   ├── services/
|   |   ├── api.js
|   |   └── documentService.js
|   |
|   ├── App.jsx
|   ├── index.css
|   └── main.jsx
|
├── public/
|
├── package.json
├── vite.config.js
└── index.html

Frontend Development

To run the frontend locally, install the required dependencies and start the Vite development server.

npm install
npm run dev

The Vite development server starts the React application locally.

The frontend then communicates with the configured FastAPI backend.

Frontend Deployment

The React + Vite frontend is deployed using Netlify.

The deployment flow is:

React + Vite
      |
      v
Production Build
      |
      v
Netlify
      |
      v
VITE_API_BASE_URL
      |
      v
Render Backend

The frontend is deployed separately from the backend and communicates with the deployed FastAPI service through REST APIs.

Frontend Role in the Complete System

The frontend acts as the presentation and interaction layer of the Tata Legal AI system.

It connects the user with the complete backend processing pipeline.

                    React Frontend
                          |
                          v
                     FastAPI API
                          |
                          v
                  Document Processing
                          |
              +-----------+-----------+
              |                       |
              v                       v
        OCR / Parsing         Clause Extraction
                                      |
                                      v
                                RAG Retrieval
                                      |
                                      v
                                  ChromaDB
                                      |
                                      v
                                 Gemini LLM
                                      |
                                      v
                                Risk Analysis
                                      |
                                      v
                                Human Review
                                      |
                                      v
                                 SQLite DB
                                      |
                                      v
                                 API Response
                                      |
                                      v
                              React Frontend

The frontend therefore provides the complete user-facing layer, while the backend performs document processing, OCR, parsing, clause extraction, RAG retrieval, AI analysis, risk assessment, human approval, and database persistence.

## Deployment

The Tata Legal AI Document Intelligence System is deployed using a modern cloud-based architecture.

### Frontend
- **Platform:** Netlify
- **Technology:** React + Vite
- The frontend provides the user interface for PDF upload, document analysis, risk assessment, clause extraction, and AI-generated results.

### Backend
- **Platform:** Render
- **Technology:** FastAPI + Python
- The backend exposes REST APIs for document processing, OCR, RAG retrieval, and AI analysis.

### Containerization
- **Docker** is used to package the backend and its system dependencies.
- **Tesseract OCR** is installed inside the Docker container for scanned/image-based PDF processing.
- **Poppler** is used for PDF-to-image conversion during OCR processing.

### AI & RAG
- **Google Gemini API** is used for LLM-based analysis.
- **Gemini Embedding (`gemini-embedding-001`)** is used for semantic embeddings.
- **ChromaDB** is used as the vector database for storing and retrieving relevant legal document chunks.
- **LangChain** is used to implement the RAG workflow.

### Deployment Flow

Frontend (Netlify)
        ↓
FastAPI Backend (Render)
        ↓
Docker Container
        ↓
PDF Processing + OCR
        ↓
RAG Retrieval using ChromaDB
        ↓
Gemini LLM
        ↓
Legal Analysis & Risk Assessment
        ↓
Results displayed on Frontend


## LIVE LINKS :

### 🔗 Live Links

- **Frontend:** https://eclectic-biscotti-bca046.netlify.app/
- **Backend:** https://skyai-squads-aco3.onrender.com/
- **GitHub Repository:** https://github.com/Hariom-codes/SkyAI-Squads

## Team Contribution

1. **Hariom Upadhyay : Team Leader/Group Representative, Product Testing & Solution, RAG & LangChain & Vector Database, LLM, Backend, Frontend, Deployment**<br><br>

2. **Tanvi Rathore : Backend Handling, Backend-Frontend Integration, SQLite Database Handling**<br><br>

3. **Poojitha Gaddam : OCR Handling**<br><br>

4. **Mohmd Amaan Zaidi : Parsing**<br><br>

5. **Prabhat Kumar Sasmal : Clause Extraction**<br><br>

6. **Jyoti : RAG & LangChain & LLM Handling**<br><br>

7. **Vishwajith Sonawane : Human Approval Handling**<br><br>

8. **Suryansh : Frontend & Backend Deployment**<br><br>

9. **Anas Khan : Frontend Handling**<br><br>

10. **Shivaji, Vipul, Hitesh : Additional Contribution**


## 🏁 Project Conclusion

The Tata Legal AI Document Intelligence System provides an AI-powered solution for simplifying and accelerating legal document analysis. It combines **OCR, PDF parsing, clause extraction, Retrieval-Augmented Generation (RAG), LangChain, vector search, and Large Language Models (LLMs)** to process complex legal documents and generate meaningful insights.

The system helps identify important clauses, retrieve relevant legal knowledge, assess potential risks, and present the results through an easy-to-use interface. The integration of **Gemini, ChromaDB, and modern cloud deployment technologies** makes the solution practical and scalable.

Overall, the project demonstrates how **Generative AI and RAG can be applied to the legal domain** to reduce manual effort, improve information retrieval, and support faster and more structured legal decision-making.
