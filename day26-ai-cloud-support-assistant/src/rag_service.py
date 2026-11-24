
import json
import os
import sys
from pathlib import Path

# Locate the repository and existing Day25 RAG pipeline.
REPO_DIR = Path(__file__).resolve().parents[2]
RAG_DIR = REPO_DIR / "day25-rag-pipeline" / "lab2-rag-pipeline"

# The Day25 pipeline uses a relative path for its knowledge chunks.
os.chdir(RAG_DIR)
sys.path.insert(0, str(RAG_DIR))

from rag_pipeline import retrieve, build_context, build_prompt
from model_service import generate_response


def main():
    if len(sys.argv) < 2:
        raise ValueError("A user query is required.")

    query = sys.argv[1].strip()

    if not query:
        raise ValueError("Query cannot be empty.")

    # Step 1: Retrieve relevant knowledge.
    results = retrieve(query, top_k=3)

    # Step 2: Build context and augmented prompt.
    context = build_context(results)
    prompt = build_prompt(query, context)

    # Step 3: Generate the assistant response.
    model_result = generate_response(
        query,
        context,
        results
    )

    # Step 4: Return structured output.
    response = {
        "query": query,
        "retrieved_documents": results,
        "context": context,
        "prompt": prompt,
        "answer": model_result["answer"],
        "model": model_result["model"],
        "sources": model_result["sources"]
    }

    print(json.dumps(response))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
