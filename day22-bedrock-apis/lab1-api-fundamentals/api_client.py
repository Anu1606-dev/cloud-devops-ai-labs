import json
import urllib.request
import urllib.error
import time

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch_post():
    start_time = time.time()

    try:
        request = urllib.request.Request(
            API_URL,
            headers={"Accept": "application/json"},
            method="GET"
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            status_code = response.status
            response_body = response.read().decode("utf-8")
            latency = round((time.time() - start_time) * 1000, 2)

            data = json.loads(response_body)

            print("API REQUEST SUCCESSFUL")
            print("-" * 35)
            print(f"Status Code : {status_code}")
            print(f"Latency    : {latency} ms")
            print(f"Content-Type: {response.headers.get('Content-Type')}")
            print(f"Post ID    : {data['id']}")
            print(f"Title      : {data['title']}")
            print(f"Body       : {data['body']}")

    except urllib.error.HTTPError as error:
        print(f"HTTP Error: {error.code}")
        print(f"Reason    : {error.reason}")

    except urllib.error.URLError as error:
        print(f"Connection Error: {error.reason}")

    except TimeoutError:
        print("Request timed out.")

    except json.JSONDecodeError:
        print("Error: Server returned invalid JSON.")

if __name__ == "__main__":
    fetch_post()
