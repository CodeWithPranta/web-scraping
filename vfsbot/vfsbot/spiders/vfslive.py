import scrapy
import json
from pathlib import Path

class VfsliveSpider(scrapy.Spider):
    name = "vfslive"
    allowed_domains = ["api.schengenvisaappointments.com"]
    start_urls = ["https://api.schengenvisaappointments.com/api/visa-list/"]

    def parse(self, response):
        print(response.text) 
        # Parse the JSON response
        slots = response.json()

        # Define the path to the JSON file where you store the data
        json_file = Path("visa_data.json")

        # Load existing data if the file exists
        if json_file.exists():
            with open(json_file, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Compare and identify changed or new slots
        new_data = []
        for slot in slots:
            if slot not in existing_data:
                new_data.append(slot)

        # Update the JSON file with new or changed data
        if new_data:
            updated_data = existing_data + new_data
            with open(json_file, "w", encoding="utf-8") as file:
                json.dump(updated_data, file, indent=4, ensure_ascii=False)

        # Yield the new data to Scrapy logs (optional)
        for item in new_data:
            yield item
