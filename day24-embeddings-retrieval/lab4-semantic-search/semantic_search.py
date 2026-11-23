from pathlib import Path
import numpy as np
from fastembed import TextEmbedding

# Load the embedding model (CPU-based)
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Read document chunks created in Lab 2
chunk_dir = Path("../lab2-chunking/chunks")
chunk_files = sorted(chunk_dir.glob("chunk_*.txt"))

documents = []
for file in chunk_files:
    documents.append(file.read_text(encoding="utf-8"))

# Generate document embeddings
doc_embeddings = np.array(list(model.embed(documents)))

# Semantic search function
def semantic_search(query, top_k=3):
    query_embedding = np.array(list(model.embed([query])))[0]

    # Cosine similarity
    scores = np.dot(doc_embeddings, query_embedding) / (
        np.linalg.norm(doc_embeddings, axis=1)
        * np.linalg.norm(query_embedding)
    )

    ranked = np.argsort(scores)[::-1][:top_k]

    print(f"\nQuery: {query}")
    print("-" * 50)

    for idx in ranked:
        print(f"Document: {chunk_files[idx].name}")
        print(f"Similarity score: {scores[idx]:.4f}")
        print(documents[idx][:250].replace("\n", " "))
        print()

# Test semantic retrieval
queries = [
    "processor load",
    "available RAM memory",
    "resolve backend hostname DNS",
    "storage full write logs disk",
    "Linux service crashed unavailable"
]

for query in queries:
    semantic_search(query)
