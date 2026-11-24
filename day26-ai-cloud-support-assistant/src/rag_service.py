
import json
import os
import sys
from pathlib import Path

# Locate the repository and existing Day25 RAG pipeline.
REPO_DIR = Path(__file__).resolve().parents[2]
RAG_DIR = REPO_DIR / "day25-rag-pipeline" / "lab2-rag-pipeline"

# The existing pipeline uses a relative path for its knowledge chunks.
# Change the working directory before importing it.
os.chdir(RAG_DIR)
sys.path.insert(0, str(RAG_DIR))

from rag_pipeline import retrieve, build_context, build_prompt


def main():
    if len(sys.argv) < 2:
        raise ValueError("A user query is required.")

    query = sys.argv[1].strip()

    if not query:
        raise ValueError("Query cannot be empty.")

    results = retrieve(query, top_k=3)
    context = build_context(results)
    prompt = build_prompt(query, context)

    response = {
        "query": query,
        "retrieved_documents": results,
        "context": context,
        "prompt": prompt
    }

    print(json.dumps(response))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
