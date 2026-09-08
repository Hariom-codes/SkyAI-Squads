#  IMPORTANT — PROJECT EVALUATION NOTE

Please note that the `backend` and `frontend` folders available directly at the repository root are older/previous versions.

For evaluation, please use the **current and final Tata Legal AI implementation** located at:

 **[Open Current Tata Legal AI Project](https://github.com/Hariom-codes/SkyAI-Squads/tree/main/Tata-Legal-AI-Demo-Ready-Corrected-v2%20-%20Copy/Tata-Legal-AI-Demo-Ready-Corrected-v2%20copy)**

This folder contains the current integrated version of the Tata Legal AI project, including the latest backend, frontend, AI workflow, RAG pipeline, human review workflow, and document persistence/retrieval implementation.

# TATA GROUP : AI Legal Document Intelligence System

## Team Name

**SkyAI-Squads**

## 👥 Team Members

- **Hariom Upadhyay** — Group Representative
- **Tanvi Rathore**
- **Anas Jameel**
- **Poojitha Gaddam**
- **Mohd Amaan Zaidi**
- **Prabhat Kumar Sasmal**
- **Jyoti Yadav**
- **Vishwajit Sonawane**
- **Suryansh Chaurasiya**
- **Shivaji Chaudhary**
- **Vipul Kumar**
- **Hitesh Shrivastava**

> Team roles and individual responsibilities are documented in the project presentation.

## Project Overview

Tata Legal AI is an AI-powered Legal Document Intelligence System designed to simplify the analysis of complex legal documents.

The system allows users to upload legal PDF documents and uses Artificial Intelligence, OCR, document parsing, clause extraction, Retrieval-Augmented Generation (RAG), vector databases, and Large Language Models (LLMs) to analyze the document and identify important legal information and potential risks.

The solution also includes a human approval workflow, allowing AI-generated results to be reviewed before a final decision is made.

## Objective

The main objective of Tata Legal AI is to build an intelligent and efficient system that can assist users in understanding and analyzing legal documents.

The system aims to:

* Automate legal document processing and analysis.
* Extract text from both normal and scanned PDF documents.
* Identify important legal clauses.
* Retrieve relevant information from a dedicated legal knowledge base.
* Use RAG and LLMs to generate contextual legal analysis.
* Identify potential risks and concerns in legal documents.
* Provide a human-in-the-loop approval mechanism.
* Reduce the time and effort required for initial legal document review.

## Solution

Tata Legal AI provides an end-to-end AI-powered workflow for legal document intelligence.

The solution processes a legal document through multiple stages:

```text
Legal PDF
    ↓
OCR / Text Extraction
    ↓
Document Parsing
    ↓
Clause Extraction
    ↓
RAG Retrieval
    ↓
Legal Knowledge Base
    ↓
LLM Analysis
    ↓
Risk Identification
    ↓
Human Review
    ↓
Approval / Rejection
```

This integrated approach combines automated AI processing with human review to provide a structured and practical legal document analysis solution.

## Our Product

Tata Legal AI is our complete Legal Document Intelligence product that brings document processing, AI analysis, risk identification, and human approval into a single platform.

Users can upload a legal PDF and obtain structured AI-assisted insights from the document.

### Key Product Capabilities

* Legal PDF upload and processing
* OCR for scanned documents
* Document parsing
* Legal clause extraction
* 30-PDF legal knowledge base
* Retrieval-Augmented Generation (RAG)
* Gemini-based embeddings
* ChromaDB vector search
* LangChain integration
* Gemini LLM analysis
* Legal risk analysis
* Human approval workflow
* SQLite-based approval records
* Web-based frontend
* FastAPI backend
* REST API integration

## Live Project

### Frontend

**Live Frontend:**
https://eclectic-biscotti-bca046.netlify.app/

### Backend API

**Live Backend:**
https://skyai-squads-aco3.onrender.com/

### GitHub Repository

**GitHub Repository:**
[https://github.com/Hariom-codes/SkyAI-Squads](https://github.com/Hariom-codes/SkyAI-Squads/tree/main/Tata-Legal-AI-Demo-Ready-Corrected-v2%20-%20Copy/Tata-Legal-AI-Demo-Ready-Corrected-v2%20copy)


---

## Team Contributions

1. **Hariom Upadhyay** — Team Leader / Group Representative, Product Testing and Solution, RAG, LangChain, Vector Database, LLM, Backend, Frontend and Deployment.

2. **Tanvi Rathore** — Backend Handling, Backend–Frontend Integration and SQLite Database Handling.

3. **Poojitha Gaddam** — OCR Handling and Text Extraction.

4. **Mohmd Amaan Zaidi** — Legal Document Parsing.

5. **Prabhat Kumar Sasmal** — Legal Clause Extraction.

6. **Jyoti** — RAG, LangChain and LLM Handling.

7. **Vishwajith Sonawane** — Human Approval and Review Handling.

8. **Suryansh** — Frontend and Backend Deployment.

9. **Anas Khan** — Frontend Handling and User Interface Development.

10. **Shivaji** — Additional Project Contributions.

11. **Vipul** — Additional Project Contributions.

12. **Hitesh** — Additional Project Contributions.



# Backend

Backend service for the **Tata Legal AI Legal Document Intelligence System**.

The backend is built with **Python and FastAPI** and provides the complete document-processing workflow: PDF validation, OCR-based text extraction, clause parsing, RAG-based legal knowledge retrieval, Gemini-based clause analysis, human approval workflow, and document-result persistence and retrieval.

---

## 1. Backend Overview

```text
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
```

The backend exposes these capabilities through REST APIs and provides interactive API documentation through Swagger/OpenAPI.

---

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

**Embedding model:**

```text
all-MiniLM-L6-v2
```

**Vector database:**

```text
ChromaDB
```

**Collection:**

```text
tata_legal_knowledge
```

The prototype uses a local ChromaDB knowledge base. Knowledge-base materials should be maintained according to the team's agreed reference materials and access classification.

---

## 6. Gemini AI Configuration

The backend uses **Google Gemini** through the `google-genai` Python SDK.

**Current model:**

```text
gemini-3.5-flash-lite
```

**Required environment variable:**

```env
GEMINI_API_KEY=your_gemini_api_key
```

The API key must remain private and must never be committed to GitHub.

---

## 7. Human Approval Workflow

AI-generated analysis is not automatically treated as final approved legal work.

A reviewer can:

- View pending clauses
- Accept an analysis
- Reject an analysis
- Edit the reviewed text
- Escalate a clause for further review

This provides a human-in-the-loop workflow around the AI-generated analysis.

---

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


# RAG & Langchain Pipeline

###Done by : Hariom (GR) & Tanvi

## Retrieval-Augmented Generation (RAG)

<details>
<summary><strong>Click to expand RAG implementation details</strong></summary>

### Overview

Tata Legal AI uses Retrieval-Augmented Generation (RAG) to ground AI-based legal document analysis in the project's dedicated legal knowledge base.

The RAG pipeline retrieves relevant legal information from the knowledge base and provides that information as context to the Large Language Model before generating an analysis.

This reduces the need for the LLM to rely only on its pretrained knowledge and allows the system to use project-specific legal reference material.

### RAG Architecture

```text
Legal Knowledge Base
        ↓
PDF Documents
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
Semantic Similarity Search
        ↓
Relevant Legal Context
        ↓
Gemini LLM
        ↓
AI-Assisted Legal Analysis
```

### Legal Knowledge Base

The project uses a dedicated legal knowledge base containing legal reference PDF documents.

The documents are processed and converted into smaller text chunks before being embedded and stored in the vector database.

The purpose of the knowledge base is to provide relevant legal context during AI-assisted document analysis.

### Document Processing

The RAG pipeline begins by loading and processing the legal documents.

The general workflow is:

```text
PDF
 ↓
Text Extraction
 ↓
Document Objects
 ↓
Text Splitting
 ↓
Chunks
```

The extracted content is divided into smaller sections so that individual pieces of relevant legal information can be efficiently embedded and retrieved.

### Text Chunking

Large legal documents cannot always be passed directly to an LLM or efficiently searched as complete documents.

Therefore, the system divides documents into smaller chunks.

Chunking provides several benefits:

* Improves semantic retrieval.
* Reduces unnecessary context.
* Allows relevant sections to be retrieved independently.
* Makes large legal documents easier to search.
* Helps preserve useful context around legal clauses.

The chunking stage is implemented as part of the LangChain-based document processing pipeline.

### Gemini Embeddings

The later RAG implementation uses Google's Gemini embedding model:

```text
Model: gemini-embedding-001
Embedding Dimension: 768
```

The embedding model converts legal text into numerical vector representations.

Each document chunk is transformed into a 768-dimensional vector.

Conceptually:

```text
Legal Text Chunk
       ↓
gemini-embedding-001
       ↓
768-Dimensional Vector
```

These vectors represent the semantic meaning of the legal text and allow the system to perform semantic similarity searches.

### Document and Query Embeddings

The embedding process is used for both the stored legal documents and user queries.

```text
Legal Document Chunk
        ↓
Gemini Embedding
        ↓
768-D Vector
        ↓
ChromaDB


User Query
        ↓
Gemini Embedding
        ↓
768-D Query Vector
        ↓
Similarity Search
```

Because documents and queries are represented in the same embedding space, the system can retrieve semantically related legal information even when the wording is not exactly identical.

### Retrieval

Once the user's query or document analysis request reaches the RAG layer, the query is converted into an embedding.

The vector database then searches for the most relevant stored legal chunks.

```text
User Query
    ↓
Query Embedding
    ↓
Vector Similarity Search
    ↓
Relevant Legal Chunks
    ↓
Retrieved Context
```

The retrieved information is then passed to the generation stage.

### ChromaDB Vector Store

ChromaDB is used as the vector database for the RAG system.

Its role is to:

* Store document embeddings.
* Store associated document chunks.
* Maintain document metadata.
* Perform semantic similarity search.
* Retrieve relevant legal information.

The RAG architecture therefore separates knowledge storage from language generation:

```text
Legal Knowledge
      ↓
Gemini Embeddings
      ↓
ChromaDB
      ↓
Retrieval
      ↓
Gemini LLM
```

### Context Retrieval

The retrieved legal chunks are combined into a context that is provided to the LLM.

```text
Retrieved Chunk 1
       +
Retrieved Chunk 2
       +
Retrieved Chunk 3
       ↓
Combined Legal Context
       ↓
LLM Prompt
```

The purpose of this stage is to ensure that the LLM receives relevant project-specific legal information before generating its response.

### RAG in Legal Risk Analysis

RAG is particularly important for the project's legal risk analysis workflow.

When a clause is analyzed, the system can retrieve relevant legal reference information and provide it as context for the AI analysis.

The overall process can be represented as:

```text
Uploaded Legal Document
          ↓
Clause Extraction
          ↓
Clause / Query
          ↓
Gemini Query Embedding
          ↓
ChromaDB Retrieval
          ↓
Relevant Legal Knowledge
          ↓
Context + Clause
          ↓
Gemini LLM
          ↓
Risk Analysis
```

This allows the system to combine information from the uploaded document with relevant information from the project's legal knowledge base.

### Benefits of RAG

The RAG architecture provides several advantages:

* Project-specific legal knowledge retrieval.
* Semantic rather than exact keyword-based search.
* Better contextual grounding.
* Reduced dependence on unsupported model knowledge.
* Ability to update the knowledge base independently of the LLM.
* Traceability of retrieved legal reference material.
* Better support for domain-specific legal analysis.

</details>

---

## LangChain

<details>
<summary><strong>Click to expand LangChain implementation details</strong></summary>

### Overview

LangChain is used as the orchestration and integration framework connecting the major components of the RAG and LLM pipeline.

It provides common interfaces for document processing, embeddings, vector stores, retrieval, prompts, and language models.

The integration can be represented as:

```text
Documents
    ↓
LangChain Document Processing
    ↓
Text Splitter
    ↓
Embedding Interface
    ↓
ChromaDB
    ↓
Retriever
    ↓
Prompt / Context
    ↓
Gemini LLM
```

### LangChain Responsibilities

Within Tata Legal AI, LangChain is used to integrate:

* Document processing.
* Text splitting.
* Embedding interfaces.
* Vector database integration.
* Retrieval.
* Prompt construction.
* LLM communication.
* RAG orchestration.

### Document Integration

Legal documents are represented in a format that can be processed through LangChain components.

This allows the downstream RAG pipeline to work consistently with document content and metadata.

### Embedding Integration

The Gemini embedding model is integrated into the vector retrieval architecture so that legal document chunks can be converted into vectors before being stored in ChromaDB.

```text
Legal Text
    ↓
Gemini Embedding
    ↓
768-Dimensional Vector
    ↓
ChromaDB
```

LangChain provides the abstraction layer that allows the embedding component to work with the vector store.

### ChromaDB Integration

LangChain provides the integration between the RAG pipeline and ChromaDB.

The vector store is responsible for:

```text
Embedding Storage
        ↓
Vector Search
        ↓
Relevant Document Retrieval
```

This allows the application to query the legal knowledge base through a retriever rather than implementing the complete vector-search mechanism manually.

### Retriever

The retriever acts as the connection between the user's query and the stored legal knowledge.

```text
User Query
    ↓
Retriever
    ↓
ChromaDB
    ↓
Relevant Documents
```

The retrieved documents are then passed to the RAG generation stage.

### Prompt and Context Integration

LangChain helps combine the retrieved context with the user's query before sending the request to the LLM.

Conceptually:

```text
Retrieved Legal Context
          +
User / Clause Query
          ↓
      Prompt
          ↓
      Gemini LLM
```

This allows the LLM to generate responses based on the retrieved legal information.

### LLM Integration

LangChain also provides the interface through which the application communicates with the LLM.

The architecture separates retrieval from generation:

```text
ChromaDB
   ↓
Retriever
   ↓
Context
   ↓
LangChain
   ↓
Gemini LLM
   ↓
Response
```

### Why LangChain?

LangChain provides a modular architecture that makes it easier to connect and manage different AI components.

For Tata Legal AI, this makes it possible to maintain a pipeline where:

* The embedding model can be managed independently.
* ChromaDB handles vector storage and retrieval.
* Retrieval remains separate from generation.
* The LLM can receive structured context.
* Individual pipeline components can be modified without redesigning the complete system.

</details>

---

## Gemini Embeddings

<details>
<summary><strong>Click to expand Gemini embedding implementation</strong></summary>

### Embedding Model

The RAG system uses:

```text
Google Gemini Embedding Model
gemini-embedding-001
```

The embedding output is:

```text
768 dimensions
```

### Purpose

Embeddings convert human-readable legal text into numerical representations that capture semantic relationships.

For example:

```text
"Termination of the agreement"
```

and

```text
"Conditions under which the contract may be terminated"
```

can be represented as vectors that are semantically related even though their wording differs.

### Embedding Pipeline

```text
Legal Text
    ↓
Gemini Embedding API
    ↓
768-Dimensional Vector
    ↓
ChromaDB
```

### Query Embedding

When a user asks a question, the query is also converted into an embedding.

```text
User Question
     ↓
gemini-embedding-001
     ↓
768-D Query Vector
     ↓
Similarity Search
```

The vector database then compares this query representation with the stored legal document vectors.

### Semantic Search

The use of embeddings enables semantic retrieval instead of relying only on exact keyword matching.

```text
Keyword Search
    → Looks for matching words

Semantic Search
    → Looks for matching meaning
```

This is particularly useful for legal documents because the same legal concept can be expressed using different terminology.

</details>

---

## Large Language Model (LLM)

<details>
<summary><strong>Click to expand Gemini LLM implementation details</strong></summary>

### Overview

The Large Language Model is the generation and reasoning layer of Tata Legal AI.

The RAG pipeline retrieves relevant legal information first. The retrieved information is then provided to the Gemini LLM along with the relevant clause or user query.

```text
Retrieved Legal Context
          +
Legal Clause / Query
          ↓
      Gemini LLM
          ↓
   AI-Generated Analysis
```

### Role of the LLM

The LLM is responsible for interpreting the retrieved legal context and generating structured AI-assisted analysis.

Within the system, the LLM can support analysis such as:

* Clause understanding.
* Clause summarization.
* Legal risk identification.
* Risk reasoning.
* Recommendation generation.
* Context-based question answering.

### RAG + LLM Workflow

```text
Legal Document
      ↓
Clause Extraction
      ↓
Clause / Query
      ↓
Gemini Query Embedding
      ↓
ChromaDB
      ↓
Relevant Legal Knowledge
      ↓
Retrieved Context
      ↓
Gemini LLM
      ↓
Structured Legal Analysis
```

### Context-Grounded Generation

The LLM receives retrieved information from the project's legal knowledge base rather than operating independently.

The conceptual prompt structure is:

```text
System Instructions
        +
Retrieved Legal Context
        +
Legal Clause / User Query
        ↓
Gemini LLM
        ↓
Generated Analysis
```

The retrieved context acts as supporting information for the generated response.

### Risk Analysis Output

For legal clause analysis, the AI analysis is structured around important fields such as:

```text
Clause Name
Summary
Risk Level
Risk Reason
Recommendation
```

This transforms raw legal text into a more structured format that can be reviewed by users.

### Example Output Structure

```json
{
  "clause_name": "Termination Clause",
  "summary": "Summary of the clause",
  "risk_level": "Medium",
  "risk_reason": "Reason for the identified risk",
  "recommendation": "Suggested action for review"
}
```

The exact output depends on the uploaded document, extracted clause, and retrieved legal context.

### LLM and Human Review

The generated analysis is intended to support human decision-making rather than replace human review.

The overall workflow is:

```text
Document
   ↓
AI Processing
   ↓
RAG Retrieval
   ↓
Gemini Analysis
   ↓
Risk Assessment
   ↓
Human Review
   ↓
Approval / Rejection
```

This creates a human-in-the-loop architecture for the legal document intelligence system.

### Separation of Responsibilities

The AI architecture separates the responsibilities of embeddings, retrieval, and generation:

| Component                                   | Responsibility                                                  |
| ------------------------------------------- | --------------------------------------------------------------- |
| **Gemini Embedding `gemini-embedding-001`** | Converts legal text and queries into 768-dimensional vectors    |
| **ChromaDB**                                | Stores embeddings and performs similarity retrieval             |
| **LangChain**                               | Connects and orchestrates the AI pipeline                       |
| **Gemini LLM**                              | Interprets retrieved context and generates AI-assisted analysis |
| **Human Reviewer**                          | Reviews AI output and makes the final approval decision         |

### Complete AI Pipeline

```text
                 LEGAL PDF
                    │
                    ▼
             Document Processing
                    │
                    ▼
              Clause Extraction
                    │
                    ▼
              Query / Clause
                    │
                    ▼
        ┌─────────────────────────┐
        │ Gemini Embedding        │
        │ gemini-embedding-001    │
        │ 768 Dimensions          │
        └────────────┬────────────┘
                     │
                     ▼
                ChromaDB
                     │
                     ▼
            Relevant Legal Context
                     │
                     ▼
              LangChain Pipeline
                     │
                     ▼
              ┌──────────────┐
              │ Gemini LLM   │
              └──────┬───────┘
                     │
                     ▼
             Legal Risk Analysis
                     │
                     ▼
               Human Review
                     │
                     ▼
              Final Decision
```

</details>


## Deployment

The Tata Legal AI system is deployed using a separate frontend-backend architecture.

```text
                    USER
                     │
                     ▼
          React + Vite Frontend
                     │
                     │ API Requests
                     ▼
              FastAPI Backend
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      OCR          RAG          Gemini
        │            │            │
        │         ChromaDB       LLM
        │            │
        └────────────┼────────────┘
                     ▼
              JSON Response
                     │
                     ▼
               Frontend UI
```

### Frontend Deployment

The frontend is built using **React + Vite** and is deployed as a separate web application.

The frontend communicates with the deployed FastAPI backend through HTTP API requests.

**Frontend Technology:**

* React
* Vite
* JavaScript
* Tailwind CSS

**Frontend Responsibilities:**

* Legal PDF upload.
* Displaying document processing status.
* Displaying extracted clauses.
* Displaying AI-generated summaries.
* Displaying risk levels and risk reasons.
* Displaying recommendations.
* Human approval and review interface.
* Communicating with backend APIs.

### Backend Deployment

The backend is built using **FastAPI** and deployed as a cloud service.

The deployed backend provides REST APIs used by the frontend for document processing and AI-based legal analysis.

**Backend Technology:**

* Python
* FastAPI
* Uvicorn
* OCR processing
* RAG pipeline
* ChromaDB
* LangChain
* Gemini Embeddings
* Gemini LLM

### Backend Deployment URL

**Live Backend:**

[Tata Legal AI Backend](https://skyai-squads-aco3.onrender.com?utm_source=chatgpt.com)

### API Documentation

FastAPI automatically provides interactive API documentation.

For local development:

```text
http://localhost:8000/docs
```

The Swagger interface can be used to test and understand the available backend endpoints.

### Environment Variables

API keys and sensitive configuration values are stored using environment variables rather than being hard-coded into the application.

Example:

```env
GEMINI_API_KEY=your_api_key
```

The actual API key should never be committed to GitHub.

### Deployment Architecture

```text
                    Internet
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     Frontend                    Backend
   React + Vite                 FastAPI
          │                         │
          │       REST API          │
          └────────────────────────►│
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
                OCR              RAG Pipeline       Gemini
                                   │                  LLM
                                   ▼
                                ChromaDB
```

### Production Request Flow

When a user uploads a legal document:

```text
1. User uploads PDF
        ↓
2. Frontend sends request to FastAPI
        ↓
3. Backend validates the document
        ↓
4. OCR / PDF processing extracts text
        ↓
5. Clauses are identified
        ↓
6. RAG retrieves relevant legal knowledge
        ↓
7. Gemini LLM performs AI-assisted analysis
        ↓
8. Backend generates structured results
        ↓
9. Results are returned as JSON
        ↓
10. Frontend displays the analysis
        ↓
11. Human reviewer reviews the result
```

### Deployment Benefits

The separate frontend-backend deployment provides:

* Independent frontend and backend development.
* Scalable backend API architecture.
* Clear separation of presentation and business logic.
* Secure handling of API credentials through environment variables.
* Easy integration between the web interface and AI backend.
* Ability to update frontend and backend independently.

### Deployment Stack

| Layer                | Technology                    |
| -------------------- | ----------------------------- |
| **Frontend**         | React + Vite                  |
| **Frontend Hosting** | Netlify                       |
| **Backend**          | FastAPI + Python              |
| **Backend Hosting**  | Render                        |
| **API Server**       | Uvicorn                       |
| **Vector Database**  | ChromaDB                      |
| **RAG Framework**    | LangChain                     |
| **Embeddings**       | Gemini `gemini-embedding-001` |
| **LLM**              | Gemini                        |
| **Database**         | SQLite                        |
| **Version Control**  | Git + GitHub                  |

</details>


## Frontend

The Tata Legal AI frontend is built using **React + Vite** and provides the user-facing interface for uploading legal documents, viewing AI-generated analysis, and managing the human review workflow.

### Frontend Technology Stack

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| **React**        | Building the user interface            |
| **Vite**         | Frontend development and build tool    |
| **JavaScript**   | Application logic                      |
| **Tailwind CSS** | Styling and responsive UI              |
| **REST APIs**    | Communication with the FastAPI backend |

### Frontend Architecture

The frontend follows a component-based React architecture.

```text id="k6v9m1"
                    React Application
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      Components         Pages          Layouts
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    API / Services
                           │
                           ▼
                  FastAPI Backend
```

### Main Frontend Responsibilities

The frontend provides the following functionality:

* Legal PDF document upload.
* Document processing status.
* Display of extracted legal clauses.
* AI-generated clause summaries.
* Risk-level visualization.
* Risk reason and explanation.
* AI recommendations.
* Human approval and review workflow.
* Document result display.
* Communication with backend REST APIs.

### Document Upload

Users can upload a legal PDF through the frontend interface.

```text id="3n2p7q"
User
 ↓
Select Legal PDF
 ↓
Upload
 ↓
Frontend
 ↓
FastAPI API
 ↓
Backend Processing
```

The frontend sends the uploaded document to the backend, where PDF processing, OCR, clause extraction, RAG retrieval, and AI analysis are performed.

### API Integration

The React frontend communicates with the FastAPI backend through REST APIs.

The API layer handles operations such as:

```text id="b9k4t2"
PDF Upload
     ↓
POST /upload
     ↓
FastAPI Backend
     ↓
Processing
     ↓
JSON Response
     ↓
React UI
```

The frontend uses the backend response to dynamically display the document analysis results.

### Results Dashboard

After processing, the frontend presents the AI-generated results in a structured interface.

The results can include:

```text id="v8r2m6"
Document
   │
   ├── Clause Name
   ├── Clause Summary
   ├── Risk Level
   ├── Risk Reason
   └── Recommendation
```

This makes the output easier for users to understand compared with displaying raw AI-generated text.

### Risk Visualization

The frontend visually presents the risk level associated with analyzed clauses.

The interface allows users to quickly identify clauses that may require additional attention.

```text id="n4p7x2"
Legal Clause
     ↓
AI Analysis
     ↓
Risk Level
     ↓
Risk Explanation
     ↓
Recommendation
```

### Human-in-the-Loop Interface

The frontend also supports the human approval workflow.

Reviewers can interact with AI-generated results and perform actions such as:

* View pending clauses.
* Review AI analysis.
* Approve a clause.
* Reject a clause.
* Edit the AI-generated result.
* Escalate a clause for further review.

```text id="z3c8w5"
AI Analysis
     ↓
Human Review
     │
     ├── Approve
     ├── Reject
     ├── Edit
     └── Escalate
```

This ensures that the AI output can be reviewed by a human before a final decision is made.

### Frontend–Backend Communication

The frontend and backend are deployed separately but communicate through REST APIs.

```text id="p7d2k9"
┌──────────────────────────┐
│       React Frontend     │
│          + Vite          │
└────────────┬─────────────┘
             │
             │ HTTP / REST API
             ▼
┌──────────────────────────┐
│      FastAPI Backend     │
│          Python          │
└────────────┬─────────────┘
             │
     ┌───────┼────────┐
     ▼       ▼        ▼
    OCR     RAG     Gemini
             │        LLM
             ▼
          ChromaDB
```

### Frontend Project Structure

The React application is organized into reusable modules and components.

```text id="e5r8u1"
frontend/
│
├── src/
│   ├── components/
│   ├── data/
│   ├── hooks/
│   ├── i18n/
│   ├── layouts/
│   ├── pages/
│   ├── services/
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
│
├── package.json
├── vite.config.js
├── tailwind.config.js
└── postcss.config.js
```

### Component-Based Design

React components are used to divide the application into reusable UI elements.

This improves:

* Code organization.
* Maintainability.
* Reusability.
* UI consistency.
* Development efficiency.

### Responsive Interface

The frontend is designed to provide a user-friendly interface for interacting with the legal document intelligence system.

The interface organizes complex AI-generated legal information into structured sections so that users can easily understand the analysis and review the identified risks.

### Frontend Deployment

The frontend is deployed independently from the backend.

**Frontend Framework:** React + Vite

**Hosting Platform:** Netlify

The deployed frontend communicates with the production FastAPI backend through its configured API endpoint.

### Frontend Workflow

```text id="r2m6v8"
                 USER
                   │
                   ▼
            React Frontend
                   │
                   ▼
             PDF Upload
                   │
                   ▼
             FastAPI API
                   │
                   ▼
          Backend Processing
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
         OCR      RAG     Gemini
                           LLM
          │        │        │
          └────────┼────────┘
                   ▼
             JSON Response
                   │
                   ▼
             React Frontend
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       Summary    Risk   Recommendation
                   │
                   ▼
             Human Review
```

</details>


## Team Contributions

1. **Hariom Upadhyay** — Team Leader / Group Representative, Product Testing and Solution, RAG, LangChain, Vector Database, LLM, Backend, Frontend and Deployment.

2. **Tanvi Rathore** — Backend Handling, Backend–Frontend Integration and SQLite Database Handling.

3. **Poojitha Gaddam** — OCR Handling and Text Extraction.

4. **Mohmd Amaan Zaidi** — Legal Document Parsing.

5. **Prabhat Kumar Sasmal** — Legal Clause Extraction.

6. **Jyoti** — RAG, LangChain and LLM Handling.

7. **Vishwajith Sonawane** — Human Approval and Review Handling.

8. **Suryansh** — Frontend and Backend Deployment.

9. **Anas Khan** — Frontend Handling and User Interface Development.

10. **Shivaji** — Additional Project Contributions.

11. **Vipul** — Additional Project Contributions.

12. **Hitesh** — Additional Project Contributions.


## Conclusion

Tata Legal AI is an AI-powered Legal Document Intelligence System designed to simplify and accelerate the analysis of complex legal documents.

The system combines **OCR, document parsing, clause extraction, RAG, Gemini Embeddings, ChromaDB, LangChain, and Gemini LLM** to retrieve relevant legal knowledge and generate structured clause-level analysis.

By providing **summaries, risk levels, risk reasoning, and recommendations**, the system helps users identify potentially important contractual clauses more efficiently.

The integration of a **Human-in-the-Loop approval workflow** ensures that AI-generated results can be reviewed and validated by a human before making final decisions.

Overall, Tata Legal AI demonstrates how **Generative AI and Retrieval-Augmented Generation can be applied to legal document analysis** to create a more efficient, structured, and review-oriented workflow while keeping human oversight at the center of the decision-making process.


                                                              #THANK YOU
