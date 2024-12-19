from bs4 import BeautifulSoup
from urllib.request import urlopen

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    
    def print(self):
        print(f'TITLE: {self.title}')
        print(f'URL: {self.url}')
        print(f'BODY: {self.body}')

def scrapeCNN(url):
    bs = BeautifulSoup(urlopen(url))
    title = bs.find('h1').text
    body = bs.find('div', class_='article__content').text
    print('body: ')
    print(body)
    return Content(url, title, body)

url = 'https://edition.cnn.com/2024/12/17/asia/north-korean-soldiers-russia-intl-hnk/index.html'
content = scrapeCNN(url)
content.print()