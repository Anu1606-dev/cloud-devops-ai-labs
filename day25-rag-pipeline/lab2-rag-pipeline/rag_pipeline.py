from pathlib import Path
import numpy as np
from fastembed import TextEmbedding

# Load embedding model
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Load existing Day 24 chunks
chunk_dir = Path(
    "../../day24-embeddings-retrieval/lab2-chunking/chunks"
)

chunk_files = sorted(chunk_dir.glob("chunk_*.txt"))

documents = [
    file.read_text(encoding="utf-8")
    for file in chunk_files
]

# Generate embeddings for the knowledge base
doc_embeddings = np.array(list(model.embed(documents)))


def retrieve(query, top_k=3):
    query_embedding = np.array(
        list(model.embed([query]))
    )[0]

    scores = np.dot(doc_embeddings, query_embedding) / (
        np.linalg.norm(doc_embeddings, axis=1)
        * np.linalg.norm(query_embedding)
    )

    ranked_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for idx in ranked_indices:
        results.append({
            "file": chunk_files[idx].name,
            "text": documents[idx],
            "score": float(scores[idx])
        })

    return results


def build_context(results):
    context = ""

    for result in results:
        context += (
            f"\n--- Source: {result['file']} ---\n"
            f"{result['text']}\n"
        )

    return context


def build_prompt(query, context):
    return f"""
You are a Cloud Support Engineer AI assistant.

Rules:
- Use the provided context to answer.
- Never invent logs, metrics, or root causes.
- If the context does not contain enough information,
  clearly state what is missing.
- Provide safe diagnostic steps before remediation.
- Separate facts from hypotheses.

CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:
"""


if __name__ == "__main__":
    query = (
        "My Linux API is experiencing problems. "
        "The service is unavailable and requests are failing. "
        "What should I investigate?"
    )

    results = retrieve(query, top_k=3)

    print("\n===== RETRIEVED DOCUMENTS =====")

    for result in results:
        print(f"\nSource: {result['file']}")
        print(f"Similarity: {result['score']:.4f}")
        print(result["text"][:250])

    context = build_context(results)
    prompt = build_prompt(query, context)

    print("\n===== AUGMENTED PROMPT =====")
    print(prompt)
