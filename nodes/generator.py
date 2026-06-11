from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)


def generate_answer(state):

    docs = state["filtered_docs"]

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
    You are a technical documentation assistant.

    Answer ONLY using the provided context.

    Context:
    {context}

    Question:
    {state['question']}

    If the answer is not in the context,
    say:
    "I could not find the answer in the documentation."
    """

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }