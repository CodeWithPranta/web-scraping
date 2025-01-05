import requests
from bs4 import BeautifulSoup

response = requests.get('https://payment.ivacbd.com/')
html = response.content
bs = BeautifulSoup(html, 'html.parser')
print(bs)