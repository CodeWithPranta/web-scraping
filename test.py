import requests
from bs4 import BeautifulSoup

access_token = "EAAAAAYYVdQhptt7SE8kelaalA7wLbP01sSu8D33hpr8vIiLodVEmtdNw7Mmwfeif+s8WEfKfevdLtaOlnyFbxnIGH6eOJr3+w2HSE1FTF92xLFNB0yusAVX1dfvQQEdpbY7S52wRaNyUfQ4FidDdpG4HcCGsUhxhGKAnLvATlyx23vPPsv3X/L/C9rPT5Cmi1jz6FPgxBlcd6xUin/YgpjWMSpp82BH7hq65NC7Of1YVODUjEBUQ+cG3orOnxq3V8ogITGFfDnFnX+cg4dZfaCb+0pvcCnuHxOLtsTxlIHxGlVX8IvoMQ3FVpg8kgrNrb4lTR99DtZw2NNh6pQMs/6pjJuC2whM3FLL5bTEkSLPRKYDywuJAZZTP01E6kOzQadLs6Zt7cfVciIC1RCMUX02I7fjxEh1TyKLsOdCBkU2g9wsjTLpxOODoAeh0IfwF2G6aoYTWUv3rxMKbLLpGTFvadqdu4JiKaXzx3d5buis9jMNcBvJvhqK1Q2XX7tP7r1cZ8WrLq73hAjjs6/4VeF1QBo="
headers = {
    "Authorization": f"Bearer {access_token}",
}

proxy_url = "https://proxy.scrapeops.io/v1/"
proxy_params = {
    'api_key': '9913642a-f917-42bc-bc9f-814b44438fa6',
    'url': 'https://visa.vfsglobal.com/npl/en/ltp/dashboard',
}

# Login URL
application_url = proxy_url

response = requests.get(
    url=application_url,
    params=proxy_params,
    headers=headers,
)

html = response.content
bs = BeautifulSoup(html, 'html.parser')
btn = bs.find('span', class_='mdc-button__label').text.strip()
print(btn)

