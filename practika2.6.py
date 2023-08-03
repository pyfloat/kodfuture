import requests

url = 'http://dim-spo.ru'

response = requests.get(url)
response.raiseforstatus()

print(response.text)