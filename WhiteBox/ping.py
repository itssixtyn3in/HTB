import requests
import random
import string

# Function to generate a valid sid
def generate_sid(uid):
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    checksum = hex(sum(ord(c) for c in random_chars))[2:]  # Calculate checksum and convert to hex
    return uid + random_chars + checksum

# Define the uid and email
uid = "testuser"
email = "testuser@example.com"

# Generate a valid sid
sid = generate_sid(uid)
print(f"Generated SID: {sid}")

# Define URL and headers
auth_url = "http://localhost:5000/api/auth/authenticate"
ping_url = "http://localhost:5000/api/service/ping"
headers = {'Content-Type': 'application/json'}

# Create the payload with uid, sid, and email
payload = {'uid': uid, 'sid': sid, 'email': email}

# Send the authentication request
response = requests.post(auth_url, json=payload, headers=headers)

# Print the response
print(f"Authentication Response Status Code: {response.status_code}")
print(f"Authentication Response Body: {response.json()}")

# If authentication successful, proceed with ping request
if response.status_code == 200:
    token = response.json().get('token')
    print(f"Authentication successful, token: {token}")

    # Define headers with the token
    headers_with_token = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Define the payload for the ping endpoint
    ping_payload = {'external': 'true', 'ip': '{"ip": "8.8.8.8"}'}

    # Make a POST request to the ping endpoint
    ping_response = requests.post(ping_url, json=ping_payload, headers=headers_with_token)

    # Print the response
    print(f"Ping Endpoint Response Status Code: {ping_response.status_code}")
    print(f"Ping Endpoint Response: {ping_response.text}")

    if ping_response.status_code == 200:
        print("Ping command successful.")
        print(f"Ping response: {ping_response.text.strip()}")
    else:
        print("Ping command failed.")
else:
    print("Authentication failed.")
