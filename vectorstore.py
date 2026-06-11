from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    return vectordb