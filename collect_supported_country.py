import json
import requests

response = requests.get("https://api.schengenvisaappointments.com/api/visa-list/")
json_data = response.json()  # Already parsed into a list or dictionary

# No need to use json.loads() again
convert_into_dictionary = json_data

# Print and iterate over the data
print(convert_into_dictionary)
for item in convert_into_dictionary:
    print(f'source country: {item["source_country"]}, mission country: {item["mission_country"]}, and link: {item["book_now_link"]}')
