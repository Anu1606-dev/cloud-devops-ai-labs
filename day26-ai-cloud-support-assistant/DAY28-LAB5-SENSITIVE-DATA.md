# Day 28 — Lab 5: Sensitive-Data Protection

## Objective
Reduce the risk of exposing credentials in user queries, RAG responses and application diagnostics.

## 1. Redaction helper
Extended `src/security.py` with `redact_sensitive_data()`.

It detects and redacts:
- AWS access-key IDs beginning with AKIA or ASIA.
- Bearer authorization tokens.
- JWT-like tokens.
- Common password, API-key, secret and access-token assignments.

Non-string values are returned unchanged.

## 2. RAG data handling
Updated `src/rag_service.py` to sanitize:
- User queries before retrieval.
- Retrieved context before prompt construction.
- Constructed prompts before returning them.
- Generated answers before returning them.

Exception output now reports the exception type rather than printing the raw exception message.

## 3. Logging safeguards
The Node.js request logger records request IDs, HTTP method, path, status and duration. It does not log request bodies or raw query strings.

RAG backend failures log error metadata rather than raw stderr or exception messages.

## 4. Automated tests
All 12 security tests passed:
- Six prompt-injection tests.
- AWS access-key redaction.
- Bearer-token redaction.
- Password and API-key assignment redaction.
- JWT redaction.
- Preservation of ordinary troubleshooting text.
- Handling of non-string inputs.

Python syntax compilation and `git diff --check` passed.

## 5. Docker integration validation
- Updated image built successfully.
- Container started and reported healthy.
- Normal troubleshooting query returned HTTP 200.
- Sensitive AWS-key query returned HTTP 200 with the key redacted.
- Original test key was absent from the returned JSON.
- Original test key was absent from container logs.
- `/health` returned HTTP 200.
- `/ready` returned HTTP 200.

## 6. Limitations
- Pattern-based redaction is not exhaustive.
- Novel, encoded, split or unrecognized secrets may not be detected.
- The AWS key used in testing was a synthetic test value, not a real credential.
- This lab does not implement a full DLP system or external secrets scanner.
- The assistant still uses deterministic mock generation, not live LLM inference.

## Interview takeaway
"I added a reusable sensitive-data redaction layer for common credential formats and applied it to user queries, RAG context, prompts and answers. I verified the behavior with unit tests and Docker API tests, including checking that a synthetic AWS key did not appear in the response or container logs."
