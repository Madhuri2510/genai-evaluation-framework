from rag.retriever import retrieve_docs
from rag.generator import generate_response
from evaluation.evaluator import evaluate_all
from prompt_testing.prompt_tests import run_prompt_tests

def main():
    print("🚀 Running Prompt Test Suite...")
    results = run_prompt_tests()

if __name__ == "__main__":
    main()

# def main():
#     print("🚀 Starting pipeline...")

#     query = "What is intermittent fasting?"

#     print("🔍 Retrieving context...")
#     context = retrieve_docs(query)

#     print("🤖 Generating response...")
#     response = generate_response(query, context)

#     print("\n=== RESPONSE ===")
#     print(response)

#     print("\n📊 Evaluating response...")
#     result = evaluate_all(query, context, response)

#     print("\n=== EVALUATION ===")
#     print(result["scores"])

#     print("\n=== FINAL VERDICT ===")
#     print(result["verdict"])

# if __name__ == "__main__":
#     main()