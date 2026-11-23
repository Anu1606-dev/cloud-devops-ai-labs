import os

api_key = os.getenv("DEMO_API_KEY")

if not api_key:
    print("Authentication failed: API key missing")
else:
    print("Authentication configuration detected")
    print("Credential loaded securely from environment")
