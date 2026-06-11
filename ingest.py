import os
from dotenv import load_dotenv

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from langchain_huggingface import (
    HuggingFaceEmbeddings,
)

from langchain_chroma import Chroma

load_dotenv()

DOCS_PATH = "docs"
CHROMA_PATH = "chroma_db"


def load_documents():

    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.md",
        loader_cls=TextLoader
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    print("ChromaDB created successfully")

    return vectordb


def main():

    print("Loading documents...")

    documents = load_documents()

    print("Splitting documents...")

    chunks = split_documents(documents)

    if len(chunks) == 0:
        raise ValueError(
            "No chunks created. Check docs folder content."
        )

    print("Generating embeddings...")

    create_vector_store(chunks)

    print("Ingestion completed successfully")


if __name__ == "__main__":
    main()