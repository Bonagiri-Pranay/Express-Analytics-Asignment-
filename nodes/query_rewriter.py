from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)


def rewrite_query(state):

    question = state["question"]

    prompt = f"""
    Rewrite the following question to improve document retrieval.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return {
        "rewritten_question": response.content,
        "retry_count": state.get("retry_count", 0) + 1
    }