import argparse

from prompt_testing.prompt_tests import run_prompt_tests
from utils.config_loader import load_config
from utils.mlflow_logger import log_experiment


def main():
    parser = argparse.ArgumentParser(description="GenAI Evaluation Framework")

    parser.add_argument(
        "--mode",
        choices=["test", "single"],
        default="test",
        help="Run mode: test suite or single query"
    )

    args = parser.parse_args()

    config = load_config()

    print("🚀 Starting GenAI Framework...")
    print("Mode:", args.mode)

    if args.mode == "test" and config["run_prompt_tests"]:
        results = run_prompt_tests()

    elif args.mode == "single":
        from rag.retriever import retrieve_docs
        from rag.generator import generate_response
        from evaluation.evaluator import evaluate_all

        query = input("Enter your query: ")

        context = retrieve_docs(query)
        response = generate_response(query, context)
        evaluation = evaluate_all(query, context, response)
        # 🔥 Log to MLflow
        log_experiment(query, response, evaluation, config)

        print("\nResponse:", response)
        print("\nEvaluation:", evaluation)

    print("\n✅ Execution complete")


if __name__ == "__main__":
    main()