import requests
import json
import re
import time

# Telegram Bot Token
BOT_TOKEN = "7414817026:AAGavLA5stpYOvRUQWg5grxSy2nXwK4ssgE"  # Replace with your bot's token

# List of Chat IDs (Replace with actual chat IDs of users)
CHAT_IDS = ["6369309742", "7536947314",]  # Add as many IDs as needed

MAX_MESSAGE_LENGTH = 4096  # Telegram's maximum message length

# Track the last sent data for each country
last_sent_data = {}

# Function to send messages to Telegram
def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Message sent successfully to Chat ID {chat_id}!")
        else:
            print(f"Failed to send message to Chat ID {chat_id}. Error: {response.text}")
    except Exception as e:
        print(f"Error sending message to Chat ID {chat_id}: {e}")

# Function to split a long message into chunks
def split_message(message):
    return [message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]

# Function to escape special characters in Telegram Markdown
def escape_markdown(text):
    if text is None:
        return "Not Available"  # Replace None with a default value
    return re.sub(r'([_*[\]()~`>#+\-=|{}.!])', r'\\\1', str(text))  # Ensure text is a string

# Format JSON data into a Telegram message
def format_message(entry):
    try:
        return (
            f"🌍 *Source Country:* {escape_markdown(entry.get('source_country'))}\n"
            f"🏛️ *Mission Country:* {escape_markdown(entry.get('mission_country'))}\n"
            f"📄 *Visa Category:* {escape_markdown(entry.get('visa_category'))}\n"
            f"🔖 *Visa Subcategory:* {escape_markdown(entry.get('visa_subcategory'))}\n"
            f"📍 *Center:* {escape_markdown(entry.get('center_name'))}\n"
            f"📅 *Appointment Date:* {escape_markdown(entry.get('appointment_date'))}\n"
            f"👥 *People Looking:* {escape_markdown(entry.get('people_looking'))}\n"
            f"🔗 [Book Now]({entry.get('book_now_link', 'https://example.com')})\n"
            f"🕒 *Last Checked:* {escape_markdown(entry.get('last_checked'))}\n"
        )
    except Exception as e:
        print(f"Error formatting message: {e}")
        return "Error formatting message."

# Fetch updated JSON data
def fetch_data():
    try:
        response = requests.get("https://api.schengenvisaappointments.com/api/visa-list/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Compare current data with the last sent data
def check_for_updates(json_data):
    global last_sent_data
    updated_countries = []

    for entry in json_data:
        # Filter only for source_country Ghana and mission_country France
        if entry.get('source_country') == 'Ghana' and entry.get('visa_subcategory') == 'Tourist':
            # Use a unique key (e.g., source_country + mission_country) to track changes
            key = f"{entry.get('source_country', 'Unknown')}->{entry.get('mission_country', 'Unknown')}"
            
            # Check if the data has changed
            if key not in last_sent_data or last_sent_data[key] != entry:
                updated_countries.append(entry)
                last_sent_data[key] = entry  # Update the stored data
    
    return updated_countries

# Main function to run the process every 2 minutes
def main():
    while True:
        json_data = fetch_data()
        if json_data:
            updated_entries = check_for_updates(json_data)
            if updated_entries:
                for entry in updated_entries:
                    message = format_message(entry)
                    # Split the message if it's too long
                    message_chunks = split_message(message)
                    for chunk in message_chunks:
                        # Send the message to all users
                        for chat_id in CHAT_IDS:
                            send_telegram_message(chat_id, chunk)
            else:
                print("No updates detected for Ghana -> France.")
        else:
            print("Failed to fetch data.")
        
        # Wait for 2 minutes before checking again
        time.sleep(120)

if __name__ == "__main__":
    main()
