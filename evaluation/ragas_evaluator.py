from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset


def evaluate_with_ragas(query: str, context: str, response: str):
    """
    Perform RAGAS-based evaluation for LLM responses.

    Metrics:
    - Faithfulness: Is response grounded in context?
    - Answer Relevancy: Does response answer the question?

    Returns:
        dict: RAGAS scores
    """

    try:
        # Prepare dataset in RAGAS format
        data = {
            "question": [query],
            "answer": [response],
            "contexts": [[context]]
        }

        dataset = Dataset.from_dict(data)

        # Run RAGAS evaluation
        result = evaluate(
            dataset,
            metrics=[faithfulness, answer_relevancy]
        )

        # Extract and round scores
        scores = {
            "ragas_faithfulness": round(result["faithfulness"][0], 2),
            "ragas_relevance": round(result["answer_relevancy"][0], 2)
        }

        return scores

    except Exception as e:
        # Fail-safe: prevent pipeline crash
        print("⚠️ RAGAS evaluation failed:", str(e))

        return {
            "ragas_faithfulness": None,
            "ragas_relevance": None
        }