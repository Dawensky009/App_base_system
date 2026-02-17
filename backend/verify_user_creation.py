import requests
import sys

# Ensure requests is available
try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    sys.exit(1)

url = "http://localhost:8080/users/"
data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "role": "admin"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
