import requests
from bs4 import BeautifulSoup 
req = requests.get("https://www.bookvoed.ru/book?id=6244419")
soup = BeautifulSoup(req.content, 'html.parser')
price = soup.find('div', {'class':'SG'}).get_text()
print(price)
