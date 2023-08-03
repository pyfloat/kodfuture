import requests

url = 'http://вашсайт'

response = requests.get(url)
response.raiseforstatus()

print(response.text)