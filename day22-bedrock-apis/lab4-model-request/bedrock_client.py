import boto3
import time
from botocore.stub import Stubber

REGION = "us-east-1"
MODEL_ID = "amazon.nova-lite-v1:0"

# Fake credentials are used ONLY to create a local test client.
# No real AWS authentication or network request is made.
client = boto3.client(
    "bedrock-runtime",
    region_name=REGION,
    aws_access_key_id="testing",
    aws_secret_access_key="testing"
)

prompt = "Explain cloud computing in 3 beginner-friendly bullet points."

messages = [
    {
        "role": "user",
        "content": [{"text": prompt}]
    }
]

expected_params = {
    "modelId": MODEL_ID,
    "messages": messages,
    "inferenceConfig": {
        "maxTokens": 200,
        "temperature": 0.3
    }
}

# Simulated Bedrock response
fake_response = {
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "text": (
                        "• Cloud computing provides IT resources over the internet.\n"
                        "• Resources can scale according to demand.\n"
                        "• You can pay for the resources you consume."
                    )
                }
            ]
        }
    },
    "stopReason": "end_turn",
    "usage": {
        "inputTokens": 15,
        "outputTokens": 35,
        "totalTokens": 50
    },
    "metrics": {
        "latencyMs": 1200
    }
}

# Stubber intercepts the API call and returns our fake response
stubber = Stubber(client)
stubber.add_response(
    "converse",
    fake_response,
    expected_params
)

stubber.activate()

print("Sending simulated request to Amazon Bedrock...")
start_time = time.perf_counter()

try:
    response = client.converse(
        modelId=MODEL_ID,
        messages=messages,
        inferenceConfig={
            "maxTokens": 200,
            "temperature": 0.3
        }
    )

    latency = (time.perf_counter() - start_time) * 1000

    answer = response["output"]["message"]["content"][0]["text"]
    usage = response["usage"]

    print("\nMODEL REQUEST SUCCESSFUL (SIMULATED)")
    print("-" * 40)
    print("Model:", MODEL_ID)
    print("Region:", REGION)
    print(f"Execution latency: {latency:.2f} ms")

    print("\nAI RESPONSE:")
    print(answer)

    print("\nTOKEN USAGE:")
    print("Input tokens:", usage["inputTokens"])
    print("Output tokens:", usage["outputTokens"])
    print("Total tokens:", usage["totalTokens"])

    print("\nMode: Local simulation")
    print("Real AWS request: No")

except Exception as error:
    print("\nREQUEST FAILED")
    print("Error type:", type(error).__name__)
    print("Error:", error)

finally:
    stubber.deactivate()
