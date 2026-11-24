
from security import is_suspicious_instruction


def generate_response(query, context, retrieved_documents):
    """
    Simulate an LLM response using retrieved RAG context.

    This is deterministic mock logic.
    It does NOT call an actual language model.
    """

    if not query.strip():
        raise ValueError("Query cannot be empty.")

    if not retrieved_documents or not context.strip():
        answer = (
            "Insufficient knowledge-base context was retrieved. "
            "More information is required before recommending "
            "troubleshooting actions."
        )
    else:
        # Extract diagnostic instructions directly from retrieved context.
        diagnostic_steps = []

        for line in context.splitlines():
            instruction = line.strip()

            if instruction.startswith(("Use ", "Investigate ")):
                if is_suspicious_instruction(instruction):
                    continue

                if instruction not in diagnostic_steps:
                    diagnostic_steps.append(instruction)

        if diagnostic_steps:
            steps = "\n".join(
                f"{index}. {step}"
                for index, step in enumerate(diagnostic_steps, start=1)
            )
        else:
            steps = (
                "No specific diagnostic commands were found "
                "in the retrieved context."
            )

        answer = (
            "Mock Cloud Support Assistant Response\n\n"
            f"Question: {query}\n\n"
            "Based on the retrieved knowledge-base context, "
            "consider these initial diagnostic steps:\n\n"
            f"{steps}\n\n"
            "The available context does not establish the actual "
            "root cause. Collect service logs, application metrics, "
            "and relevant infrastructure evidence before remediation."
        )

    return {
        "answer": answer,
        "model": {
            "provider": "mock",
            "mode": "simulation",
            "inference_performed": False
        },
        "sources": [
            {
                "file": document["file"],
                "score": document["score"]
            }
            for document in retrieved_documents
        ]
    }
