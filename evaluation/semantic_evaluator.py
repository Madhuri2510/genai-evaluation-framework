from sentence_transformers import SentenceTransformer, util

# Load model once (important for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_semantic_similarity(query: str, response: str):
    """
    Computes semantic similarity between query and response.
    Returns score between 0 and 1.
    """

    try:
        # Convert text to embeddings
        query_embedding = model.encode(query, convert_to_tensor=True)
        response_embedding = model.encode(response, convert_to_tensor=True)

        # Compute cosine similarity
        similarity = util.cos_sim(query_embedding, response_embedding)

        return round(float(similarity[0][0]), 2)

    except Exception as e:
        print("⚠️ Semantic similarity failed:", e)
        return None