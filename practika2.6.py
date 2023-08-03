import requests
# введите сайт своей школы
url = 'http://вашсайт' 

response = requests.get(url)
response.raiseforstatus()

print(response.text)
