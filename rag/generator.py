import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def generate_response(query: str, context: str):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    return response.content