import requests
import json

reqUrl = "http://51.222.14.197:3040/lead"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "message": "Quiero comer pollo",
  "phone": "50661650000"
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)