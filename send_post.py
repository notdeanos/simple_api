import requests

url = 'http://127.0.0.1:3002/api'
data = {'appdome': 'appdo.me123'}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
