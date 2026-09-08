# Tata Legal AI — Legal Document Intelligence System

## Project Overview

Tata Legal AI — Legal Document Intelligence System is an AI-powered solution developed by **Team SkyAI-Squads** to simplify and accelerate the analysis of legal documents.

The system is designed to process legal PDF documents and automatically extract useful information such as clauses, summaries, potential risks, supporting legal knowledge, and recommendations.

The project combines **PDF processing, OCR, text parsing, clause extraction, Retrieval-Augmented Generation (RAG), LangChain, Gemini Embeddings, ChromaDB, Google Gemini LLM, SQLite database, FastAPI, React, Docker, and cloud deployment** into a single end-to-end legal document intelligence platform.

The system follows a complete pipeline starting from document upload and ending with structured AI-generated legal insights and human review.

---

## Objective

The primary objective of the project is to reduce the manual effort involved in reviewing lengthy legal documents.

Instead of manually going through every page and clause, the system helps users:

- Upload legal documents
- Extract text from PDFs
- Process scanned documents using OCR
- Parse and structure document content
- Identify important clauses
- Retrieve relevant legal knowledge
- Analyze clauses using Generative AI
- Identify potential risks
- Generate explanations and recommendations
- Review AI-generated results through a human approval workflow
- Store processed document results
- Retrieve previous analysis using a unique document ID

The system is designed as an AI-assisted solution where human review remains an important part of the workflow.

---

## Legal Knowledge Base

The project uses a dedicated legal knowledge base containing **20 PDF documents**.

These documents provide the reference knowledge used by the RAG system during legal clause analysis.

The knowledge-base workflow is:

```text
20 Legal PDF Documents
        ↓
Document Loading
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Gemini Embeddings
        ↓
ChromaDB
        ↓
Semantic Search
        ↓
Relevant Legal Knowledge
        ↓
Gemini LLM

The knowledge base allows the system to retrieve relevant information instead of relying only on the general knowledge of the language model.

Overall System

The complete system consists of several interconnected layers.

Frontend
   ↓
FastAPI Backend
   ↓
PDF Processing
   ↓
OCR / Text Extraction
   ↓
Parsing
   ↓
Clause Extraction
   ↓
RAG Retrieval
   ↓
ChromaDB
   ↓
Gemini Embeddings
   ↓
Gemini LLM
   ↓
Risk Analysis
   ↓
Human Approval
   ↓
SQLite Database
   ↓
Result Retrieval
   ↓
Frontend

Each component performs a specific role in the overall document intelligence workflow.

Complete Document Processing Workflow
Step 1 — PDF Upload

The user uploads a legal PDF document through the frontend.

The frontend sends the document to the FastAPI backend through the document upload API.

User
 ↓
React Frontend
 ↓
POST /upload
 ↓
FastAPI Backend
Step 2 — File Validation

The backend first validates the uploaded file.

The system checks whether:

A file was uploaded
The file is a supported PDF
The document is not empty
The document can be processed

Invalid files are rejected before entering the main processing pipeline.

Step 3 — PDF Processing

The uploaded PDF is processed page by page.

For documents containing selectable text, the text can be extracted directly.

For scanned or image-based documents, OCR processing is used.

PDF
 ↓
PDF Pages
 ↓
Text Extraction / Image Conversion
OCR Processing
OCR Technology

The project uses Tesseract OCR for extracting text from scanned or image-based legal documents.

The OCR pipeline uses:

Tesseract OCR
pytesseract
pdf2image
Pillow
Poppler

The workflow is:

Scanned PDF
    ↓
PDF Pages
    ↓
Image Conversion
    ↓
Tesseract OCR
    ↓
Extracted Text

OCR allows the system to process documents where normal text extraction is not sufficient.

Text Parsing

After text extraction, the document content is passed to the parsing layer.

The parser processes the extracted text and structures the document content so that relevant clauses can be identified and analyzed.

Extracted Text
      ↓
Text Cleaning
      ↓
Text Parsing
      ↓
Structured Content

Parsing is an important stage because the AI analysis works at the clause level rather than treating the complete document as one large block of text.

Clause Extraction

After parsing, relevant legal clauses are identified from the document.

Each clause becomes an individual unit that can be processed through the AI pipeline.

The clause-processing flow is:

Document
   ↓
Parsed Text
   ↓
Clause Extraction
   ↓
Individual Clauses
   ↓
Clause Analysis

The system can then analyze each clause separately and provide information such as:

Clause name
Clause summary
Risk level
Risk reason
Recommendation
Retrieval-Augmented Generation
RAG Overview

Retrieval-Augmented Generation is one of the core components of the project.

The purpose of RAG is to provide the Gemini LLM with relevant information retrieved from the project's legal knowledge base.

Instead of sending only the clause to the LLM, the system first searches the knowledge base and retrieves relevant legal information.

Legal Clause
     ↓
Query Embedding
     ↓
ChromaDB Search
     ↓
Relevant Knowledge
     ↓
Clause + Retrieved Context
     ↓
Gemini LLM
     ↓
AI Analysis
Knowledge Base Preparation

The 20 legal PDF documents are processed before being used for retrieval.

The preparation pipeline is:

20 Legal PDFs
      ↓
Document Loading
      ↓
Text Extraction
      ↓
Document Chunking
      ↓
Gemini Embeddings
      ↓
Vector Storage
      ↓
ChromaDB

The documents are divided into smaller chunks so that relevant sections can be retrieved efficiently.

Text Chunking

Large legal documents are divided into smaller text chunks before generating embeddings.

The project uses a recursive text-splitting approach to create meaningful chunks while maintaining contextual overlap between neighboring sections.

This improves retrieval because the system can search smaller and more relevant pieces of the legal knowledge base.

Gemini Embeddings

The current RAG implementation uses:

gemini-embedding-001

Gemini Embeddings convert text into numerical vector representations.

These vectors allow the system to compare the semantic similarity between:

User Document Clause
        and
Knowledge Base Chunks

The most relevant chunks are then retrieved from ChromaDB.

ChromaDB Vector Database

The project uses ChromaDB as the vector database.

ChromaDB stores the embeddings and corresponding legal document chunks.

The retrieval process works as follows:

Legal Knowledge
      ↓
Gemini Embeddings
      ↓
ChromaDB
      ↓
Similarity Search
      ↓
Top Relevant Chunks

The retrieved chunks are then passed to the AI analysis layer.

LangChain

LangChain is used to structure and manage the RAG workflow.

It connects the different components involved in retrieval and AI processing.

The RAG architecture can be represented as:

Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
Retriever
   ↓
Relevant Context
   ↓
LLM

LangChain helps organize the retrieval pipeline and provides the connection between the vector database and the AI analysis process.

Generative AI Analysis

The project uses Google Gemini as the Large Language Model.

The LLM receives:

Legal Clause
+
Retrieved Legal Knowledge

The model then analyzes the clause and generates structured information.

AI Output

The generated analysis includes:

Clause Name
Summary
Risk Level
Risk Reason
Recommendation

This structured output is then returned to the backend and displayed through the frontend.

Risk Analysis

One of the important purposes of the AI analysis is identifying potential risks in legal clauses.

The system generates:

Risk level
Reason for the identified risk
Supporting information
Recommendation

The general workflow is:

Legal Clause
      ↓
Relevant Knowledge
      ↓
Gemini Analysis
      ↓
Risk Identification
      ↓
Risk Explanation
      ↓
Recommendation

The AI-generated risk information is intended to assist reviewers in understanding clauses more efficiently.

Human-in-the-Loop Review

The system includes a Human-in-the-Loop approval workflow.

AI-generated results are not treated as an automatic final legal decision.

A human reviewer can review the generated clause analysis.

Review Actions

The reviewer can:

View pending clauses
Approve a result
Reject a result
Edit a result
Escalate a result
Review Statuses
Pending
Approved
Rejected
Escalated

This workflow ensures that human judgment remains involved in the legal document analysis process.

SQLite Database

The project uses SQLite for storing processed document results.

After a document is successfully processed, the system generates a unique document ID.

The result is then stored in the database.

Stored Information
Document ID
Filename
Analysis Result
Created At

This allows the system to retrieve previously processed documents without requiring the same document to be processed again.

Document ID and Result Retrieval

Each processed document receives a unique identifier.

The workflow is:

PDF Upload
    ↓
Document Processing
    ↓
AI Analysis
    ↓
Unique Document ID
    ↓
SQLite Database

The stored result can later be retrieved using:

GET /documents/{document_id}

This provides persistence between document-processing sessions.

Backend

The backend is developed using Python and FastAPI.

The backend acts as the core processing layer of the application.

It connects the frontend with:

PDF processing
OCR
Parsing
Clause extraction
RAG
ChromaDB
Gemini AI
Human approval
SQLite persistence
Backend Flow
Frontend Request
      ↓
FastAPI API
      ↓
Document Processing
      ↓
OCR
      ↓
Parsing
      ↓
Clause Extraction
      ↓
RAG Retrieval
      ↓
Gemini AI
      ↓
Database
      ↓
API Response
Backend Services
Upload Service

Handles document upload and coordinates the complete document-processing pipeline.

OCR Service

Handles OCR-based text extraction from scanned documents.

Parser Service

Processes extracted text and structures document content.

RAG Service

Retrieves relevant legal knowledge from ChromaDB.

AI Service

Communicates with Google Gemini and generates clause-level analysis.

Approval Service

Handles human review actions such as approval, rejection, editing, and escalation.

Document Service

Handles SQLite persistence and document retrieval.

Frontend

The frontend is developed using React and Vite.

It provides the user interface through which users interact with the legal document intelligence system.

The frontend is responsible for:

PDF upload
Sending requests to the backend
Displaying processing results
Showing clauses
Showing risk information
Showing recommendations
Displaying AI-generated analysis
Supporting the review workflow

The frontend communicates with the FastAPI backend using REST APIs.

Frontend-Backend Integration

The frontend and backend communicate through HTTP REST APIs.

The integration works as follows:

React Frontend
      ↓
API Request
      ↓
FastAPI Backend
      ↓
Document Processing
      ↓
AI Analysis
      ↓
JSON Response
      ↓
React Frontend
      ↓
Results Displayed

The main document-processing request is:

POST /upload
API Endpoints
Basic Endpoints
GET /
GET /health
Document Processing
POST /upload
GET /documents/{document_id}
Human Approval
GET /approvals/pending
GET /approvals/{clause_id}

POST /approvals/{clause_id}/accept
POST /approvals/{clause_id}/reject
PUT /approvals/{clause_id}/edit
POST /approvals/{clause_id}/escalate
Upload API
POST /upload

The /upload endpoint is the main entry point for document processing.

The complete processing pipeline includes:

Receive PDF
Validate file
Process PDF
Perform OCR when required
Extract text
Parse document content
Extract clauses
Retrieve relevant legal knowledge
Perform Gemini AI analysis
Generate risk information
Generate recommendations
Create document ID
Store result in SQLite
Return structured response
Document Retrieval API
GET /documents/{document_id}

This endpoint retrieves a previously processed document using its unique document ID.

The workflow is:

Document ID
     ↓
SQLite Database
     ↓
Stored Analysis
     ↓
API Response
     ↓
Frontend

If the document exists, the stored result is returned to the frontend.

API Documentation

FastAPI automatically provides interactive Swagger documentation.

The local Swagger interface is available at:

http://localhost:8000/docs

Swagger can be used to:

View API endpoints
Test APIs
Upload documents
Inspect requests
Inspect responses
Test document retrieval
Test human approval APIs
Technology Stack
Category	Technology
Frontend	React + Vite
Backend	Python + FastAPI
PDF Processing	pypdf
OCR	Tesseract OCR
OCR Python Library	pytesseract
PDF to Image	pdf2image
Image Processing	Pillow
Text Processing	LangChain Text Splitters
RAG Framework	LangChain
Embedding Model	gemini-embedding-001
Vector Database	ChromaDB
LLM	Google Gemini
Database	SQLite
API	REST API
API Documentation	Swagger / OpenAPI
Containerization	Docker
Frontend Deployment	Netlify
Backend Deployment	Render
Project Architecture
Tata Legal AI
│
├── Frontend
│   └── React + Vite
│
├── Backend
│   └── FastAPI
│
├── Document Processing
│   ├── PDF Processing
│   └── OCR
│
├── Parsing
│   └── Clause Extraction
│
├── Knowledge Layer
│   ├── 20 Legal PDFs
│   ├── Text Chunking
│   ├── Gemini Embeddings
│   └── ChromaDB
│
├── AI Layer
│   └── Google Gemini LLM
│
├── Review Layer
│   └── Human Approval
│
├── Persistence Layer
│   └── SQLite
│
└── Deployment
    ├── Netlify
    ├── Render
    └── Docker
End-to-End System Flow
                    User
                     |
                     v
              React Frontend
                     |
                     v
              PDF Upload API
                     |
                     v
              FastAPI Backend
                     |
                     v
              File Validation
                     |
                     v
             PDF Processing
                     |
                     v
              OCR / Extraction
                     |
                     v
                Parsing
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
                ChromaDB
                     |
                     v
          Relevant Legal Knowledge
                     |
                     v
              Gemini LLM
                     |
                     v
              Clause Analysis
                     |
          +----------+----------+
          |                     |
          v                     v
      Risk Level          Recommendation
          |                     |
          +----------+----------+
                     |
                     v
              Human Review
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Approve    Reject     Escalate
                     |
                     v
              SQLite Database
                     |
                     v
             Document ID
                     |
                     v
            Result Retrieval
                     |
                     v
              React Frontend
Deployment

The project uses a cloud-based deployment architecture.

Frontend Deployment

The React + Vite frontend is deployed using Netlify.

The frontend provides the user-facing interface and communicates with the backend through REST APIs.

Backend Deployment

The FastAPI backend is deployed using Render.

The backend handles:

PDF processing
OCR
Parsing
Clause extraction
RAG retrieval
Gemini AI analysis
Human approval
SQLite persistence
Docker

Docker is used to create a consistent backend environment.

The Docker environment includes the required system dependencies for PDF and OCR processing.

It includes:

Python
FastAPI
Tesseract OCR
Poppler
Python dependencies
Deployment Architecture
React + Vite
     ↓
Netlify
     ↓
REST API
     ↓
FastAPI
     ↓
Render
     ↓
Docker Container
     ↓
PDF + OCR Processing
     ↓
RAG + ChromaDB
     ↓
Gemini AI
     ↓
SQLite
     ↓
API Response
     ↓
Frontend
Error Handling

The backend handles common errors during document processing.

Invalid File

Unsupported or invalid files are rejected before processing.

Empty PDF

Empty documents are rejected instead of being sent through the complete pipeline.

OCR Failure

OCR-related failures are handled and returned through appropriate API responses.

Text Extraction Failure

If meaningful text cannot be extracted from the document, the system returns an appropriate error.

No Clauses Detected

If relevant clauses cannot be identified, the backend returns an appropriate response.

Document Not Found

If an invalid document ID is requested, the API returns a not-found response.

Unexpected Processing Error

Unexpected backend errors are handled and returned as API errors instead of failing silently.

Security and Configuration

The Gemini API key is configured using environment variables.

Example:

GEMINI_API_KEY=your_gemini_api_key

Sensitive credentials are not stored directly inside the source code.

Environment files such as .env should not be committed to the GitHub repository.

Project Structure
Tata-Legal-AI/
│
├── backend/
│   │
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
│   │
│   ├── data/
│   │   └── approvals.db
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
└── frontend/
    │
    ├── src/
    ├── public/
    ├── package.json
    └── vite.config.js
Testing

The project was tested across the major stages of the application.

Document Processing Testing

The document workflow was tested from PDF upload through AI analysis.

PDF Upload
    ↓
Validation
    ↓
OCR / Text Extraction
    ↓
Parsing
    ↓
Clause Extraction
    ↓
RAG Retrieval
    ↓
Gemini Analysis
    ↓
Risk Assessment
    ↓
Recommendation
API Testing

FastAPI Swagger was used to test backend endpoints and verify request and response behavior.

Integration Testing

The frontend and backend were integrated and tested to verify that:

Documents can be uploaded
Requests reach the backend
Documents are processed
AI analysis is generated
Results are returned to the frontend
Stored documents can be retrieved
Deployment Testing

The deployed frontend and backend were tested to verify communication between the cloud services.

Development Status
Implemented Components
Legal PDF Knowledge Base
20 PDF Reference Documents
PDF Upload
File Validation
PDF Processing
OCR
Text Extraction
Parsing
Clause Extraction
RAG Pipeline
Gemini Embeddings
ChromaDB
LangChain
Gemini LLM
Risk Analysis
Recommendations
Human Approval Workflow
SQLite Persistence
Document ID Generation
Document Retrieval
FastAPI APIs
Swagger Documentation
React Frontend
Frontend-Backend Integration
Docker Configuration
Cloud Deployment
Current Status

The project provides a functional end-to-end legal document intelligence workflow covering document ingestion, OCR, parsing, clause extraction, RAG-based knowledge retrieval, Generative AI analysis, risk assessment, human review, database persistence, and frontend presentation.

Future Improvements

Potential improvements for a larger production environment include:

Enterprise authentication
Role-based access control
Advanced document versioning
Scalable database infrastructure
Scalable vector database infrastructure
Automated knowledge-base updates
Advanced monitoring and logging
Improved legal-domain evaluation
Model benchmarking
Advanced document comparison
Multi-document analysis
Enhanced audit logging
Additional security controls
Project Conclusion

The Tata Legal AI — Legal Document Intelligence System demonstrates the practical application of Generative AI and Retrieval-Augmented Generation in the legal domain.

The system combines a 20-PDF legal knowledge base, OCR, PDF processing, parsing, clause extraction, Gemini Embeddings, ChromaDB, LangChain, Gemini LLM, SQLite, FastAPI, React, Docker, and cloud deployment to create a complete legal document intelligence workflow.

The system can take a legal PDF from initial upload through text extraction, clause identification, knowledge retrieval, AI analysis, risk assessment, recommendation generation, human review, and final result storage.

The project demonstrates how AI can assist legal and compliance workflows by reducing repetitive document-review effort, improving retrieval of relevant information, and presenting complex legal content in a more structured and accessible form.

The system is designed as an AI-assisted solution, with human review remaining an important part of the overall legal decision-making process.

Disclaimer

This project is developed for demonstration, educational, and evaluation purposes.

The system is intended to assist with legal document processing, clause analysis, knowledge retrieval, and risk identification.

AI-generated results should be reviewed by a qualified legal professional before being used for actual legal decisions.

This system does not provide legal advice and does not replace professional legal judgment.

Team Contributions
Team SkyAI-Squads
1. Hariom Upadhyay

Team Leader / Group Representative, Product Testing and Solution, RAG, LangChain, Vector Database, LLM, Backend, Frontend, Deployment

2. Tanvi Rathore

Backend Handling, Backend-Frontend Integration, SQLite Database Handling

3. Poojitha Gaddam

OCR Handling

4. Mohmd Amaan Zaidi

Parsing

5. Prabhat Kumar Sasmal

Clause Extraction

6. Jyoti

RAG, LangChain and LLM Handling

7. Vishwajith Sonawane

Human Approval Handling

8. Suryansh

Frontend and Backend Deployment

9. Anas Khan

Frontend Handling

10. Shivaji, Vipul and Hitesh

Additional Project Contributions


**Is version mein exact flow ye hai:**  
**Project Name → Overview → Objective → 20 PDF Knowledge Base → OCR → Parsing → Clause Extraction → RAG → Embeddings → ChromaDB → LangChain → Gemini → Risk Analysis → Human Approval → SQLite → Backend → Frontend → APIs → Architecture → Deployment → Testing → Conclusion → Disclaimer → Team Contributions LAST.**
