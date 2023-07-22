import requests

url = 'http://192.168.0.6:3030/api'
data = {'appdome': 'appdo.me123'}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
