from vectorstore import load_vectorstore

vectordb = load_vectorstore()

def retrieve(state):

    query = state["rewritten_question"]

    docs = vectordb.similarity_search(
        query,
        k=5
    )

    return {
        "documents": docs
    }