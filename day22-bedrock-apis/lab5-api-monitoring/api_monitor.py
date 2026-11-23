import time

# Simulated API request records
requests = [
    {
        "name": "Request-01",
        "status": 200,
        "latency_ms": 850,
        "input_tokens": 120,
        "output_tokens": 250
    },
    {
        "name": "Request-02",
        "status": 429,
        "latency_ms": 120,
        "input_tokens": 100,
        "output_tokens": 0
    },
    {
        "name": "Request-03",
        "status": 403,
        "latency_ms": 95,
        "input_tokens": 80,
        "output_tokens": 0
    },
    {
        "name": "Request-04",
        "status": 500,
        "latency_ms": 2100,
        "input_tokens": 150,
        "output_tokens": 0
    },
    {
        "name": "Request-05",
        "status": 200,
        "latency_ms": 8000,
        "input_tokens": 500,
        "output_tokens": 900
    }
]

def diagnose(status, latency):
    if status == 429:
        return "THROTTLING", "Reduce request rate and review quotas"

    elif status == 403:
        return "ACCESS DENIED", "Investigate IAM permissions"

    elif status >= 500:
        return "SERVER ERROR", "Check provider health and retry safely"

    elif status >= 400:
        return "CLIENT ERROR", "Inspect request and parameters"

    elif latency >= 5000:
        return "HIGH LATENCY", "Investigate model, network and token size"

    else:
        return "HEALTHY", "No immediate action required"


total = len(requests)
success = 0
failed = 0
total_latency = 0
total_input_tokens = 0
total_output_tokens = 0

print("=" * 65)
print("             AI API MONITORING REPORT")
print("=" * 65)

for request in requests:
    start = time.perf_counter()

    # Simulate monitoring processing
    time.sleep(0.01)

    processing_time = (time.perf_counter() - start) * 1000

    status = request["status"]
    latency = request["latency_ms"]

    category, action = diagnose(status, latency)

    total_latency += latency
    total_input_tokens += request["input_tokens"]
    total_output_tokens += request["output_tokens"]

    if 200 <= status < 300:
        success += 1
    else:
        failed += 1

    print(f"\n{request['name']}")
    print(f"Status       : {status}")
    print(f"Latency      : {latency} ms")
    print(f"Input tokens : {request['input_tokens']}")
    print(f"Output tokens: {request['output_tokens']}")
    print(f"Diagnosis    : {category}")
    print(f"Action       : {action}")
    print(f"Monitor time : {processing_time:.2f} ms")

# Final metrics
avg_latency = total_latency / total
success_rate = (success / total) * 100
failure_rate = (failed / total) * 100

print("\n" + "=" * 65)
print("                  SUMMARY METRICS")
print("=" * 65)
print(f"Total requests : {total}")
print(f"Successful    : {success}")
print(f"Failed       : {failed}")
print(f"Success rate : {success_rate:.2f}%")
print(f"Failure rate : {failure_rate:.2f}%")
print(f"Average latency: {avg_latency:.2f} ms")
print(f"Input tokens : {total_input_tokens}")
print(f"Output tokens: {total_output_tokens}")
print(f"Total tokens : {total_input_tokens + total_output_tokens}")
print("=" * 65)
