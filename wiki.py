from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getLinks(pageUrl, pages=set()):
    base_url = 'http://en.wikipedia.org'
    try:
        html = urlopen(base_url + pageUrl)
    except Exception as e:
        print(f"Error fetching URL: {base_url + pageUrl} - {e}")
        return pages

    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(f"Title: {bs.h1.get_text()}")
        print(f"First paragraph: {bs.find(id='mw-content-text').find_all('p')[0].get_text()}")
        
        edit_link = bs.find(id='ca-edit')
        if edit_link:
            print(f"Edit link: {edit_link.find('a').attrs['href']}")
    except AttributeError as e:
        print(f"This page is missing something! Error: {e}")
        return pages

    for link in bs.find_all('a', href=re.compile('^/wiki/[^:]*$')):  # Ignore links with colons (e.g., /wiki/Help:)
        if 'href' in link.attrs:
            newPage = link.attrs['href']
            if newPage not in pages:
                print('-' * 20)
                print(f"Found new page: {newPage}")
                pages.add(newPage)
                pages = getLinks(newPage, pages)  # Recursive call

    return pages


# Start the crawler
getLinks('/wiki/Web_scraping')
