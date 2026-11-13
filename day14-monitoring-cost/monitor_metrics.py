import json
from pathlib import Path
from statistics import mean

file_path = Path("metrics.jsonl")

records = []

with file_path.open() as file:
    for line in file:
        records.append(json.loads(line))

if not records:
    raise SystemExit("No metrics data found.")

total_requests = len(records)

errors = [
    record for record in records
    if record["status"] >= 500
]

error_count = len(errors)
error_rate = (error_count / total_requests) * 100

latencies = [record["latency_ms"] for record in records]

average_latency = mean(latencies)
maximum_latency = max(latencies)

print("=== Application Metrics ===")
print(f"Service: {records[0]['service']}")
print(f"Invocations: {total_requests}")
print(f"Errors: {error_count}")
print(f"Error rate: {error_rate:.1f}%")
print(f"Average latency: {average_latency:.1f} ms")
print(f"Maximum latency: {maximum_latency} ms")

print("\n=== Simulated CloudWatch Alarms ===")

if error_count > 1:
    print("ErrorCount Alarm: ALARM")
else:
    print("ErrorCount Alarm: OK")

if average_latency > 500:
    print("AverageLatency Alarm: ALARM")
else:
    print("AverageLatency Alarm: OK")
