import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': '9913642a-f917-42bc-bc9f-814b44438fa6',
      'url': 'https://visa.vfsglobal.com/npl/en/ltp/login', 
  },
)

print('Response Body: ', response.content)