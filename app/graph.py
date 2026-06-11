from langgraph.graph import StateGraph, END

from app.state import GraphState

from nodes.query_rewriter import rewrite_query
from nodes.retriever import retrieve
from nodes.grader import grade_documents
from nodes.generator import generate_answer
from nodes.fallback import fallback_response


MAX_RETRIES = 2


def route_documents(state: GraphState):

    filtered_docs = state.get("filtered_docs", [])

    if len(filtered_docs) > 0:
        return "generate"

    retries = state.get("retry_count", 0)

    if retries < MAX_RETRIES:
        return "rewrite"

    return "fallback"


workflow = StateGraph(GraphState)

workflow.add_node("rewrite", rewrite_query)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade", grade_documents)
workflow.add_node("generate", generate_answer)
workflow.add_node("fallback", fallback_response)

workflow.set_entry_point("rewrite")

workflow.add_edge("rewrite", "retrieve")
workflow.add_edge("retrieve", "grade")

workflow.add_conditional_edges(
    "grade",
    route_documents,
    {
        "generate": "generate",
        "rewrite": "rewrite",
        "fallback": "fallback"
    }
)

workflow.add_edge("generate", END)
workflow.add_edge("fallback", END)

graph = workflow.compile()