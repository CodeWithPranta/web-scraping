import requests
from bs4 import BeautifulSoup

url = 'https://www.visasbot.com/'
response = requests.get(url)
html = response.content
bs = BeautifulSoup(html, 'html.parser')
visa_container = bs.find('div', id='visa-cards-container')

response2 = requests.get('https://api.schengenvisaappointments.com/api/visa-list/')
lists = response2.json()
print(lists)
print(visa_container)