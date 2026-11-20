# Day 21 — AI & LLM Foundations 🤖

## 🎯 Objective
Understand foundational AI concepts before working with AI model APIs, Amazon Bedrock, prompting, embeddings, and RAG.

## 1. AI vs ML vs Generative AI

- **Artificial Intelligence (AI):** Broad field of building systems capable of tasks associated with human intelligence.
- **Machine Learning (ML):** A subset of AI in which models learn patterns from data.
- **Generative AI (GenAI):** AI that generates new content such as text, code, images, audio, or video.

### Relationship
AI → ML → Generative AI (simplified hierarchy; not every AI technique uses ML).

## 2. Large Language Models (LLMs)

LLM stands for Large Language Model.

LLMs are deep learning models trained on large datasets to learn language patterns, process context, and generate text.

Examples: GPT, Claude, Gemini, Llama.

### Next-token prediction
An LLM generates text sequentially by predicting a likely next token based on preceding tokens and the available context. The process repeats until generation stops.

## 3. Tokens

A token is a unit of text processed by a model. It may be:
- A complete word
- A part of a word
- Punctuation
- A number
- A piece of code

One token is not necessarily one word. Tokenization varies by tokenizer and model.

### Why tokens matter
- API pricing
- Input and output limits
- Context-window capacity
- Latency and computational usage

## 4. Context Window

A context window is the token capacity available to a model for a particular processing interaction.

Context may include:
- System instructions
- User prompt
- Conversation history
- Retrieved documents
- Generated response

When context limits are reached, applications may trim messages, summarize history, chunk documents, retrieve relevant sections, or reject oversized requests.

## 5. AI Hallucinations

An AI hallucination occurs when a model generates incorrect, fabricated, unsupported, or misleading information.

### Causes
- Insufficient knowledge
- Ambiguous or incomplete prompts
- Poor or irrelevant context
- Probabilistic text generation without guaranteed fact verification

### Cloud & DevOps risks
- Incorrect Linux commands
- Fabricated CLI arguments
- Incorrect IAM permissions
- Misconfigured infrastructure
- Downtime, data loss, or security exposure

### Reduction techniques
1. Retrieval-Augmented Generation (RAG)
2. Tool calling and external verification
3. Clear instructions and uncertainty handling
4. Automated validation and testing
5. Human approval for sensitive operations

Lower temperature may reduce variability, but it does not guarantee correctness or eliminate hallucinations.

## 6. LLM API Request–Response Architecture

Typical flow:

User → AI Application → API Request → LLM → API Response → Application → User

### Request parameters

| Parameter | Purpose |
|---|---|
| Model | Selects the model to process the request |
| Messages / Prompt | Input instructions and user content |
| System instructions | Behavior and constraints |
| Max output tokens | Limits generated output |
| Temperature | Influences output variability |
| Credentials | Authenticates the application |

API structures differ between providers.

### Request vs Response
- **Request:** Data sent to the model provider.
- **Response:** Generated output and accompanying metadata returned to the application.

### HTTP 429 — Too Many Requests
Possible causes:
- Request-rate limits
- Token-rate limits
- Quota exhaustion
- Excessive concurrency
- Retry loops

Troubleshooting:
- Inspect API quotas and usage
- Check request frequency and concurrency
- Identify repeated retries
- Reduce request bursts
- Implement exponential backoff and retry limits

## 7. Key Interview Questions

**Q1. What is AI?**
AI is the field of building systems that perform tasks associated with human intelligence, such as language understanding, pattern recognition, and decision-making.

**Q2. How does ML differ from traditional programming?**
Traditional programming uses explicitly defined rules, while ML learns patterns from data to make predictions or decisions.

**Q3. What is Generative AI?**
GenAI creates new content, such as text, images, code, or audio, based on patterns learned during training.

**Q4. What is an LLM?**
An LLM is a large language model trained to learn language patterns, process context, and generate text.

**Q5. What is next-token prediction?**
The model predicts a likely next token based on preceding tokens and continues generating sequentially.

**Q6. What is a token?**
A token is a text unit processed by a model. It may represent a word, part of a word, punctuation, or other text.

**Q7. What is a context window?**
The maximum token capacity available to a model during a processing interaction.

**Q8. What is an AI hallucination?**
An incorrect or unsupported output presented as if it were factual.

**Q9. How can hallucinations be reduced?**
Using RAG, trusted context, tool verification, clear prompts, testing, and human review.

**Q10. What is an API's role in AI applications?**
It allows an application to communicate with a hosted model by sending structured requests and receiving generated responses.

**Q11. What does max output tokens control?**
It limits the maximum number of tokens generated in the model's response.

**Q12. What does HTTP 429 indicate?**
The API is rejecting requests due to rate limits or quota constraints. Investigate request frequency, token usage, concurrency, and quota.

## 8. Practical Engineering Principles

- Never blindly trust generated commands.
- Verify cloud infrastructure changes before execution.
- Protect API credentials.
- Monitor token usage and costs.
- Handle rate limits and timeouts.
- Ground AI responses in trusted information when accuracy matters.
- Use human approval for high-impact operations.

## 9. Day 21 Assessment

- Lab 1 — AI vs ML vs GenAI: 10/10
- Lab 2 — LLM Foundations: 10/10
- Lab 3 — Tokens & Context Window: 10/10
- Lab 4 — Hallucinations: 10/10
- Lab 5 — API Request & Response: 10/10

**Final score: 50/50 (100%) 🏆**

## 10. Next Day

**Day 22 — Model APIs + Amazon Bedrock**

Next: Understand how to connect applications to hosted AI models, API authentication, model invocation, and the AWS Bedrock ecosystem.

---

*Cloud + AI Learning Journey · Day 21/30 🌻*
