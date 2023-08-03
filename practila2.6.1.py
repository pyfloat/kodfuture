import requests
# введите сайт своей школы
url = 'http://вашсайт'

response = requests.get(url)
response.raise_for_status()

start_index = response.text.find("<title>") + len("<title>")
end_index = response.text.find("</title>", start_index)

title = response.text[start_index:end_index]

print(title)