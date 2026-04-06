import re

def calculate_relevance(query: str, response: str):
    query_words = set(query.lower().split())
    response_words = set(response.lower().split())

    overlap = query_words.intersection(response_words)

    score = len(overlap) / len(query_words) if query_words else 0
    return round(score, 2)


def calculate_faithfulness(context: str, response: str):
    context_words = set(context.lower().split())
    response_words = set(response.lower().split())

    supported = response_words.intersection(context_words)

    score = len(supported) / len(response_words) if response_words else 0
    return round(score, 2)


def detect_hallucination(context: str, response: str):
    context_words = set(context.lower().split())
    response_words = set(response.lower().split())

    unsupported = response_words - context_words

    # Ignore common stop words (basic cleanup)
    stopwords = {"the", "is", "and", "a", "of", "to", "in"}
    unsupported = unsupported - stopwords

    return len(unsupported) > 5  # threshold


def evaluate_all(query, context, response):
    relevance = calculate_relevance(query, response)
    faithfulness = calculate_faithfulness(context, response)
    hallucination = detect_hallucination(context, response)

    scores = {
        "relevance": relevance,
        "faithfulness": faithfulness,
        "hallucination": hallucination
    }

    verdict = final_verdict(scores)

    return {
        "scores": scores,
        "verdict": verdict
    }
    
def final_verdict(scores):
    if scores["hallucination"]:
        return "❌ FAIL: Hallucination detected"
    elif scores["faithfulness"] < 0.5:
        return "⚠️ WARNING: Low faithfulness"
    elif scores["relevance"] < 0.5:
        return "⚠️ WARNING: Low relevance"
    else:
        return "✅ PASS: Response is reliable"