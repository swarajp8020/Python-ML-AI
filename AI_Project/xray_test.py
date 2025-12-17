import requests
url = "http://127.0.0.1:8000/review"
my_data = { "code": "print('testing')" }
print("--- Sending Order Request ---")
response = requests.post(url, json=my_data)
print("\n-- XRAY: what did we send?--")
print(f"URL Target: {response.request.url}")
print(f"The 'stamp' (Content-Type): {response.request.headers['Content-Type']}")
print(f"The Body size: {response.request.headers['Content-Length']} bytes")

print("\n-- XRAY: What did server reply? --")
print(f"Status Code: {response.status_code}")
print(f"server type: {response.headers['server']}")
print(f"The Answer: {response.json()}")