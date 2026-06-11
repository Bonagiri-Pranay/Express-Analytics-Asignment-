from typing import TypedDict, List, Optional
from langchain_core.documents import Document


class GraphState(TypedDict):
    question: str
    rewritten_question: Optional[str]
    documents: List[Document]
    filtered_docs: List[Document]
    answer: Optional[str]
    retry_count: int