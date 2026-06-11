from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)


def grade_documents(state):

    question = state["question"]

    relevant_docs = []

    for doc in state["documents"]:

        prompt = f"""
        Question:
        {question}

        Document:
        {doc.page_content}

        Is this document relevant to answering the question?

        Reply ONLY with:
        relevant

        or

        irrelevant
        """

        response = llm.invoke(prompt)

        result = response.content.lower().strip()

        if result == "relevant":
            relevant_docs.append(doc)

    return {
        "filtered_docs": relevant_docs
    }