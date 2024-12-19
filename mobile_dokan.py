import requests
from bs4 import BeautifulSoup

base_url = 'https://www.mobiledokan.co/products/'
response = requests.get(base_url)
response.encoding = 'utf-8'
html = response.content
bs = BeautifulSoup(html, 'html.parser')
next_page_button = bs.find('a', class_='next page-numbers')
get_total_page_element = next_page_button.find_previous_sibling('a')
last_page_number = get_total_page_element.text.strip()
# Convert last page number into an integer
last_page_number = int(last_page_number) + 1

for i in range(1, last_page_number):
    if next_page_button is not None:
        url = base_url + 'page/' + str(i)
        response = requests.get(url)
        response.encoding = 'utf-8'
        html = response.content
        bs = BeautifulSoup(html, 'html.parser')
        # Get all products container on pages
        products = bs.find_all('div', class_='aps-product-box')

        for product in products:
            title_element = product.find('h2', class_='aps-product-title')
            # title_texts = title_element.find('a').text.strip()
            # print(title_texts)
            title_urls = title_element.find('a')['href']
            response = requests.get(title_urls)
            response.encoding = 'utf-8'
            html = response.content
            bs = BeautifulSoup(html, 'html.parser')
            product_info = bs.find('div', class_='aps-main-features')

            price = product_info.find('span', class_='aps-price-value').text.strip()
            brand_element = product_info.find('span', class_='aps-product-brand')
            brand = brand_element.find('a').text.strip()
            category_element = product_info.find('span', class_='aps-product-cat')
            category = category_element.find('a').text.strip()
            added = product_info.find('span', class_='aps-product-added').text.strip()
            updated = product_info.find('span', class_='aps-product-updated').text.strip()
            status = product_info.find('div', class_='aps-status').text.strip()


            print(price)
            print(brand)
            print(category)
            print(added)
            print(updated)
            print(status)

        print(url)


print(next_page_button)
print(get_total_page_element)
print(last_page_number)
print(type(last_page_number))