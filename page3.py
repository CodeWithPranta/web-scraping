from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img', {'src':re.compile(r'\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
    print(image['src'])

