# json-rpc/client.py
import requests
import json

def remote_min(a, b):
    payload = {
        "jsonrpc": "2.0",
        "method": "min",
        "params": [a, b],
        "id": 1
    }
    response = requests.post(
        "http://localhost:9001",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )
    return response.json()["result"]

# Tests
if __name__ == "__main__":
    print(remote_min(10, 5))   # → 5
    print(remote_min(-3, 7))   # → -3
    print(remote_min(0, 0))    # → 0