import json

# Simulated AI API responses
responses = [
    "TIMEOUT",
    "RATE_LIMIT",
    "TIMEOUT"
]

max_attempts = 3


def call_ai(attempt):
    response = responses[attempt - 1]

    if response == "TIMEOUT":
        raise TimeoutError("AI request timed out")

    if response == "RATE_LIMIT":
        raise RuntimeError("HTTP 429 - Rate limit exceeded")

    return response


for attempt in range(1, max_attempts + 1):
    print(f"\nAttempt {attempt}/{max_attempts}")

    try:
        response = call_ai(attempt)

        # Validate returned JSON
        data = json.loads(response)

        if "answer" not in data:
            raise ValueError("Required field 'answer' missing")

        print("SUCCESS:", data["answer"])
        break

    except TimeoutError as e:
        print("TIMEOUT:", e)

    except RuntimeError as e:
        print("API ERROR:", e)

    except (json.JSONDecodeError, ValueError) as e:
        print("INVALID RESPONSE:", e)

    if attempt < max_attempts:
        delay = 2 ** (attempt - 1)
        print(f"Retrying... simulated backoff: {delay}s")

else:
    print("\nAll attempts failed. Request abandoned.")
