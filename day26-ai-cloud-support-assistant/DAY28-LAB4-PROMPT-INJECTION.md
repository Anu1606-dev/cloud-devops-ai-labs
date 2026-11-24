# Day 28 — Lab 4: Prompt-Injection Defence

## Objective
Introduce basic safeguards against prompt-injection attempts in the RAG assistant.

## 1. Input screening
Created `src/security.py` with regular-expression checks for common instruction-override and secret-disclosure phrases.

The RAG service checks user input before retrieval. Detected requests receive a safe response, with no documents retrieved.

## 2. Prompt isolation
Updated the RAG prompt to distinguish trusted security instructions from untrusted retrieved context and user questions.

Retrieved documents are reference material, not instructions that can override the assistant's rules.

## 3. Retrieved instruction filtering
The mock response generator checks candidate diagnostic instructions and excludes those matching known suspicious patterns.

## 4. Automated tests
The unit tests cover:
- Instruction-override detection.
- Secret-disclosure detection.
- Normal troubleshooting questions.
- Untrusted context and question markers in the prompt.
- Filtering of suspicious retrieved instructions.
- Confirmation that the model adapter remains a mock.

The prompt-builder test loads only the required function, avoiding unnecessary NumPy and FastEmbed dependencies in the WSL test environment.

## 5. Docker validation
- Normal troubleshooting query returned HTTP 200.
- Normal query reported `input_screening: passed`.
- Malicious instruction-override query returned a safe blocked response.
- Malicious query reported `input_screening: blocked`.
- No documents were retrieved for the blocked query.
- `/health` returned HTTP 200.
- `/ready` returned HTTP 200.
- Docker container remained healthy.

## 6. Limitations
- Regex screening detects known patterns and can miss novel or obfuscated attacks.
- False positives are possible.
- Prompt delimiters and instructions improve separation but do not guarantee isolation.
- Retrieved-instruction filtering is a basic heuristic, not a semantic security classifier.
- The application still uses deterministic mock generation; no live LLM inference was tested.

## Interview takeaway
"I added basic prompt-injection screening before retrieval, marked retrieved context and user input as untrusted in the RAG prompt, and filtered suspicious retrieved instructions. I validated normal and malicious requests through automated tests and the Dockerized API."
