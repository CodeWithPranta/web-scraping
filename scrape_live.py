import requests
import time
import json

# Function to fetch JSON data from the API
def fetch_data():
    try:
        response = requests.get("https://api.schengenvisaappointments.com/api/visa-list/")
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to check and update only if data is changed
def monitor_json_data():
    # Load the previously stored data from a file or initialize an empty dictionary
    try:
        with open("previous_data.json", "r") as file:
            previous_data = json.load(file)
    except FileNotFoundError:
        previous_data = {}

    while True:
        print("Fetching new data...")
        live_data = fetch_data()
        if live_data is None:  # If fetching failed, skip this iteration
            time.sleep(120)  # Wait for 2 minutes before retrying
            continue

        # Compare the new data with the previous data
        if live_data != previous_data:
            print("Data updated! Updating the JSON file...")
            with open("previous_data.json", "w") as file:
                json.dump(live_data, file, indent=4)
            previous_data = live_data  # Update the previous_data variable
        else:
            print("No changes detected.")

        # Wait for 2 minutes before fetching again
        time.sleep(120)

# Run the monitoring function
if __name__ == "__main__":
    monitor_json_data()
