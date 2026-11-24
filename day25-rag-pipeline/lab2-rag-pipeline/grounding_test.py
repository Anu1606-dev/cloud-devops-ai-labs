def validate_answer(answer, context):
    checks = {
        "context_present": bool(context.strip()),
        "no_unsupported_root_cause": (
            "root cause cannot be determined" in answer.lower()
            or "root cause is not yet established" in answer.lower()
            or "insufficient evidence" in answer.lower()
        ),
        "safe_diagnostics": any(
            word in answer.lower()
            for word in [
                "check",
                "inspect",
                "review",
                "verify",
                "investigate"
            ]
        )
    }

    return checks


context = """
Service troubleshooting:
Check service status.
Inspect application logs.
Verify upstream connectivity.
"""

answer = """
A 503 error does not establish a root cause.
Inspect application logs, verify service health,
and check upstream connectivity.
The root cause is not yet established.
"""

results = validate_answer(answer, context)

print("===== GROUNDING VALIDATION =====")

for check, passed in results.items():
    print(f"{check}: {'PASS' if passed else 'FAIL'}")

print(
    "\nOverall:",
    "PASS" if all(results.values()) else "FAIL"
)
