from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import graph

app = FastAPI(
    title="Technical Documentation Assistant",
    version="1.0"
)


class QueryRequest(BaseModel):
    question: str


class FeedbackRequest(BaseModel):
    answer_id: str
    rating: str
    comment: str | None = None


@app.get("/")
def root():
    return {
        "message": "Technical Documentation Assistant Running"
    }


@app.post("/query")
def query(req: QueryRequest):

    result = graph.invoke(
        {
            "question": req.question,
            "rewritten_question": "",
            "documents": [],
            "filtered_docs": [],
            "answer": "",
            "retry_count": 0
        }
    )

    return {
        "question": req.question,
        "answer": result["answer"]
    }


@app.get("/documents")
def list_documents():

    return {
        "documents": [
            "fastapi_docs.md",
            "langgraph_docs.md",
            "pydantic_docs.md"
        ]
    }


@app.post("/feedback")
def feedback(req: FeedbackRequest):

    return {
        "status": "success",
        "message": "Feedback received",
        "rating": req.rating
    }