from rag_pipeline import retrieve, build_context, build_prompt


def simulated_llm(prompt):
    """
    Simulates the LLM generation stage.
    This is NOT a real AI model call.
    """

    if "CONTEXT:" not in prompt:
        return "No context was provided."

    if "service" in prompt.lower():
        return (
            "Based on the retrieved troubleshooting context, "
            "begin by checking service status and application "
            "logs. Verify whether the process is running and "
            "inspect upstream dependencies. The root cause "
            "cannot be determined without additional evidence."
        )

    return (
        "The retrieved context should be reviewed before "
        "making a diagnosis. More evidence is required."
    )


query = "My Linux API is returning errors. How should I investigate?"

# Step 1: Retrieve documents
results = retrieve(query, top_k=3)

# Step 2: Build context
context = build_context(results)

# Step 3: Augment prompt
prompt = build_prompt(query, context)

# Step 4: Send to generation adapter
answer = simulated_llm(prompt)

print("\n===== USER QUERY =====")
print(query)

print("\n===== RETRIEVED SOURCES =====")
for result in results:
    print(result["file"])

print("\n===== GENERATED RESPONSE (SIMULATION) =====")
print(answer)

