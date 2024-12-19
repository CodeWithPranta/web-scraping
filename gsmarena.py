import requests
from bs4 import BeautifulSoup

url = "https://www.gsmarena.com/"
response = requests.get(url)
response.encoding = 'utf-8'  # Ensure proper encoding

html = response.text
bs = BeautifulSoup(html, 'html.parser')

# Locate the target <div> with the desired class
brand_menu_div = bs.find('div', class_='brandmenu-v2 light l-box clearfix')

print(response.text)

print(brand_menu_div)

# Locate the <ul> inside the <div>
if brand_menu_div:
    ul_tag = brand_menu_div.find('ul')
    if ul_tag:
        # Extract all brand names from <li> elements inside the <ul>
        for li in ul_tag.find_all('li'):
            brand_name = li.find('a').get_text(strip=True)
            print(brand_name)
else:
    print("Brand menu not found!")
