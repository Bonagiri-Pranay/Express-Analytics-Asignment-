## Environment Variables

Create a `.env` file in the project root and add:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Obtain a Gemini API key from Google AI Studio.

The `.env` file is intentionally excluded from the repository for security reasons.



# RAG-Based Technical Documentation Assistant

A Retrieval-Augmented Generation (RAG) system built using LangGraph, FastAPI, ChromaDB, and Gemini. The application answers questions from technical documentation while using a self-corrective workflow that validates retrieved documents before generating responses.

---

## Project Overview

This project implements a technical documentation assistant that:

- Accepts natural language questions
- Retrieves relevant document chunks from a vector database
- Grades retrieved documents for relevance
- Generates grounded answers with citations
- Uses a LangGraph workflow with conditional routing
- Exposes functionality through FastAPI

---

## Architecture

### Workflow

```text
User Query
     |
     v
Query Rewriter
     |
     v
Retriever
     |
     v
Document Grader
     |
     +----------------+
     | Relevant Docs? |
     +----------------+
       |          |
      Yes        No
       |          |
       v          v
 Generation   Rewrite Query
       |
       v
 Final Answer
```

### Components

#### Query Analysis

- Rewrites user questions
- Improves retrieval quality

#### Retrieval

- Searches ChromaDB
- Returns Top-K document chunks

#### Document Grading

- Uses Gemini to determine relevance
- Filters irrelevant chunks

#### Generation

- Generates final answer
- Uses only validated context

#### Fallback

- Returns a safe response when no relevant documents are found

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Workflow | LangGraph |
| LLM | Gemini 2.0 Flash |
| Embeddings | Gemini Embeddings |
| Vector Store | ChromaDB |
| API | FastAPI |
| Language | Python |

---

## Project Structure

```text
rag-doc-assistant/
│
├── app/
│   ├── __init__.py
│   ├── graph.py
│   ├── main.py
│   └── state.py
│
├── nodes/
│   ├── __init__.py
│   ├── query_rewriter.py
│   ├── retriever.py
│   ├── grader.py
│   ├── generator.py
│   └── fallback.py
│
├── docs/
│   ├── fastapi_docs.md
│   ├── langgraph_docs.md
│   └── pydantic_docs.md
│
├── chroma_db/
│
├── vectorstore.py
├── ingest.py
├── requirements.txt
├── .env
└── README.md
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository_url>
cd rag-doc-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Document Ingestion

Run:

```bash
python ingest.py
```

This:

1. Loads documents from `docs/`
2. Splits documents into chunks
3. Creates embeddings
4. Stores embeddings in ChromaDB

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### POST /query

Request

```json
{
  "question": "What is FastAPI?"
}
```

Response

```json
{
  "question": "What is FastAPI?",
  "answer": "FastAPI is a modern Python framework..."
}
```

---

### GET /documents

Response

```json
{
  "documents": [
    "fastapi_docs.md",
    "langgraph_docs.md",
    "pydantic_docs.md"
  ]
}
```

---

### POST /feedback

Request

```json
{
  "answer_id": "1",
  "rating": "thumbs_up",
  "comment": "Helpful answer"
}
```

Response

```json
{
  "status": "success"
}
```

---

## Chunking Strategy

The system uses:

- Chunk Size: 1000 characters
- Chunk Overlap: 200 characters

Reasoning:

- Preserves technical context
- Reduces information loss between chunks
- Improves retrieval quality

---

## Embedding Strategy

Model:

```text
models/embedding-001
```

Reason:

- Good semantic understanding
- Fast inference
- Native Gemini support

---

## Design Decisions

### Why LangGraph?

LangGraph provides:

- Stateful workflows
- Conditional routing
- Retry mechanisms
- Easy expansion for advanced RAG patterns

### Why ChromaDB?

- Lightweight
- Easy local setup
- Good performance for small and medium datasets

### Why Gemini?

- Strong reasoning performance
- Cost effective
- Free tier available

---

## Future Improvements

- Hallucination Detection Node
- Web Search Fallback
- Session Memory
- Streamlit UI
- Hybrid Retrieval (BM25 + Vector Search)
- Reranking Layer

---

## Example Questions

- What is FastAPI?
- What are conditional edges in LangGraph?
- What is BaseModel in Pydantic?
- How does FastAPI use Pydantic?

---

## Author

Pranay Bonagiri
AI/ML Engineer Internship Assignment