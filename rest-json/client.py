# rest-json/client.py
import requests

def remote_reverse(text):
    payload = {"value": text}
    response = requests.post(
        "http://localhost:9002/reverse",
        json=payload
    )
    return response.json()["result"]

# Tests
if __name__ == "__main__":
    print(remote_reverse("hello"))      # → olleh
    print(remote_reverse("Python"))     # → nohtyP
    print(remote_reverse("123!@#"))     # → #@~321
    print(remote_reverse(""))           # → ""