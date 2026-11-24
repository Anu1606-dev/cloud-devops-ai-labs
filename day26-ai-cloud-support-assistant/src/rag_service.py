
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
from security import contains_prompt_injection, redact_sensitive_data


def main():
    if len(sys.argv) < 2:
        raise ValueError("A user query is required.")

    query = redact_sensitive_data(sys.argv[1].strip())

    if not query:
        raise ValueError("Query cannot be empty.")

    # Reject common prompt-injection attempts before retrieval.
    if contains_prompt_injection(query):
        print(json.dumps({
            "query": query,
            "retrieved_documents": [],
            "context": "",
            "prompt": "",
            "answer": (
                "This request contains instructions that the assistant "
                "cannot follow. Please submit a normal cloud troubleshooting "
                "question without attempts to override system instructions "
                "or disclose protected information."
            ),
            "model": {
                "provider": "mock",
                "mode": "simulation",
                "inference_performed": False
            },
            "sources": [],
            "security": {
                "input_screening": "blocked"
            }
        }))
        return

    # Step 1: Retrieve relevant knowledge.
    results = retrieve(query, top_k=3)

    # Step 2: Build context and augmented prompt.
    context = redact_sensitive_data(build_context(results))
    prompt = redact_sensitive_data(build_prompt(query, context))

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
        "answer": redact_sensitive_data(model_result["answer"]),
        "model": model_result["model"],
        "sources": model_result["sources"],
        "security": {
            "input_screening": "passed"
        }
    }

    print(json.dumps(response))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"RAG service failed: {type(error).__name__}", file=sys.stderr)
        sys.exit(1)
