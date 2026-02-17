import requests
import sys

# Ensure requests is available
try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    sys.exit(1)

base_url = "http://localhost:8080"
user_url = f"{base_url}/users/"
token_url = f"{base_url}/token"
docs_url = f"{base_url}/docs"

# 1. Test Docs
try:
    response = requests.get(docs_url)
    if response.status_code == 200:
        print("SUCCESS: OpenAPI Docs are accessible at /docs")
    else:
        print(f"FAILURE: Failed to access OpenAPI Docs: {response.status_code}")
except Exception as e:
    print(f"ERROR accessing Docs: {e}")

# Data for test user
test_user = {
    "username": "auth_test_user_v2",
    "email": "authtest_v2@example.com",
    "password": "securepassword123", # Plain text
    "role": "admin"
}

# 2. Create User (if not exists)
# Note: In real world we would check if exists first or handle 400, but here we just try
print("\nAttempting to create user...")
import json
print(f"Sending payload: {json.dumps(test_user)}")

response = requests.post(user_url, json=test_user)
if response.status_code == 200:
    print(f"SUCCESS: User created: {response.json()}")
elif response.status_code == 400: # 400 if already exists is fine for this test
    print(f"WARNING: User already exists (OK): {response.text}")
else:
    print(f"FAILURE: Failed to create user: {response.text}")

# 3. Test Login (Get Token)
print("\nAttempting to login...")
login_data = {
    "username": test_user["username"],
    "password": test_user["password"]
}
response = requests.post(token_url, data=login_data)
if response.status_code == 200:
    token = response.json()
    print("SUCCESS: Login successful! Token received.")
    print(f"Token: {token['access_token'][:20]}...")
else:
    print(f"FAILURE Login failed: {response.status_code} - {response.text}")
