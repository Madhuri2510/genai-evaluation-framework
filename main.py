from rag.retriever import retrieve_docs
from rag.generator import generate_response

def main():
    print("🚀 Starting pipeline...")

    query = "What is intermittent fasting?"

    print("🔍 Retrieving context...")
    context = retrieve_docs(query)
    print("Context:", context)

    print("🤖 Generating response...")
    response = generate_response(query, context)

    print("\n=== RESPONSE ===")
    print(response)

if __name__ == "__main__":
    main()