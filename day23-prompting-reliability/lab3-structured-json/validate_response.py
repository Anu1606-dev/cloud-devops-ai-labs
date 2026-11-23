import json

# Load the JSON response
with open("response.json", "r") as file:
    data = json.load(file)

# Validate required fields
required_fields = [
    "issue",
    "severity",
    "possible_causes",
    "diagnostic_commands",
    "root_cause_confirmed",
    "needs_more_information"
]

for field in required_fields:
    if field not in data:
        raise ValueError(f"Missing field: {field}")

# Validate data types
assert isinstance(data["issue"], str)
assert isinstance(data["severity"], str)
assert isinstance(data["possible_causes"], list)
assert isinstance(data["diagnostic_commands"], list)
assert isinstance(data["root_cause_confirmed"], bool)
assert isinstance(data["needs_more_information"], bool)

print("JSON validation successful!")
print("Issue:", data["issue"])
print("Severity:", data["severity"])
print("Diagnostic commands:", len(data["diagnostic_commands"]))
