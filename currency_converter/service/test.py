import requests

URL = "http://127.0.0.1:5000/convert"

data = {
    "curr_from":"USD", 
    "curr_to":"EUR", 
    "amount": 1000
}

response = requests.post(URL, json=data)

print("Response Status Code: ", response.status_code)
print("Response Content: ", response.text)
    
    