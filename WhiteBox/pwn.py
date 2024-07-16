import requests
import random
import string

# Function to generate a valid sid
def generate_sid(uid):
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    checksum = hex(sum(ord(c) for c in random_chars))[2:]  # Calculate checksum and convert to hex
    return uid + random_chars + checksum

# Define the uid
uid = "testuser"
email = "testuser@example.com"  # Define the email address

# Generate a valid sid
sid = generate_sid(uid)
print(f"Generated SID: {sid}")

# Define URLs and headers
auth_url = "http://localhost:5000/api/auth/authenticate"
hostname_url = "http://localhost:5000/api/service/hostname"
id_url = "http://localhost:5000/api/service/id"
ping_url = "http://localhost:5000/api/service/ping"
whoami_url = "http://localhost:5000/api/service/whoami"
date_url = "http://localhost:5000/api/service/date"
ls_url = "http://localhost:5000/api/service/ls"
headers = {'Content-Type': 'application/json'}

# Create the payload with uid, sid, and email
payload = {'uid': uid, 'sid': sid, 'email': email}

# Send the authentication request
response = requests.post(auth_url, json=payload, headers=headers)

# Print the response
print(f"Authentication Response Status Code: {response.status_code}")
print(f"Authentication Response Body: {response.json()}")

if response.status_code == 200:
    token = response.json().get('token')
    print(f"Authentication successful, token: {token}")

    # Define headers with the token
    headers_with_token = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Make a POST request to the hostname endpoint
    hostname_response = requests.post(hostname_url, headers=headers_with_token)

    # Print the response
    print(f"Hostname Endpoint Response Status Code: {hostname_response.status_code}")
    print(f"Hostname Endpoint Response: {hostname_response.text}")

    if hostname_response.status_code == 200:
        print("The hostname command was successful.")
        print(f"Hostname: {hostname_response.text.strip()}")
    else:
        print("The hostname command failed.")

    # Make a POST request to the id endpoint
    id_response = requests.post(id_url, headers=headers_with_token)

    # Print the response
    print(f"ID Endpoint Response Status Code: {id_response.status_code}")
    print(f"ID Endpoint Response: {id_response.text}")

    if id_response.status_code == 200:
        print("The id command was successful.")
        print(f"ID: {id_response.text.strip()}")
    else:
        print("The id command failed.")

    # Define the payload for the ping endpoint
    ping_payload = {'external': 'true', 'ip': '{"ip": "8.8.8.8"}'}

    # Make a POST request to the ping endpoint
    ping_response = requests.post(ping_url, json=ping_payload, headers=headers_with_token)

    # Print the response
    print(f"Ping Endpoint Response Status Code: {ping_response.status_code}")
    print(f"Ping Endpoint Response: {ping_response.text}")

    if ping_response.status_code == 200:
        print("The ping command was successful.")
        print(f"Ping response: {ping_response.text.strip()}")
    else:
        print("The ping command failed.")

    # Make a POST request to the whoami endpoint
    whoami_response = requests.post(whoami_url, headers=headers_with_token)

    # Print the response
    print(f"Whoami Endpoint Response Status Code: {whoami_response.status_code}")
    print(f"Whoami Endpoint Response: {whoami_response.text}")

    if whoami_response.status_code == 200:
        print("The whoami command was successful.")
        print(f"Whoami: {whoami_response.text.strip()}")
    else:
        print("The whoami command failed.")

    # Define the payload for the date endpoint
    date_payload = {'format': '%Y-%m-%d'}

    # Make a POST request to the date endpoint
    date_response = requests.post(date_url, json=date_payload, headers=headers_with_token)

    # Print the response
    print(f"Date Endpoint Response Status Code: {date_response.status_code}")
    print(f"Date Endpoint Response: {date_response.text}")

    if date_response.status_code == 200:
        print("The date command was successful.")
        print(f"Date: {date_response.text.strip()}")
    else:
        print("The date command failed.")

    # Define the payload for the ls endpoint
    ls_payload = {'path': '/'}

    # Make a POST request to the ls endpoint
    ls_response = requests.post(ls_url, json=ls_payload, headers=headers_with_token)

    # Print the response
    print(f"LS Endpoint Response Status Code: {ls_response.status_code}")
    print(f"LS Endpoint Response: {ls_response.text}")

    if ls_response.status_code == 200:
        print("The ls command was successful.")
        print(f"LS: {ls_response.text.strip()}")
    else:
        print("The ls command failed.")
else:
    print("Authentication failed.")
