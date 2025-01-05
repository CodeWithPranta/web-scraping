import requests
import json
import re
import time

# Telegram Bot Token
BOT_TOKEN = "7414817026:AAGavLA5stpYOvRUQWg5grxSy2nXwK4ssgE"  # Replace with your bot's token

# List of Chat IDs (Replace with actual chat IDs of users)
CHAT_IDS = ["6369309742", "7536947314", "1500641135", "7157931070"]

# Telegram's maximum message length
MAX_MESSAGE_LENGTH = 4096

# Track the last sent data for each country
last_sent_data = {}

def send_telegram_message(chat_id, message):
    """Send a message to a Telegram chat."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Message sent to Chat ID {chat_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Chat ID {chat_id}: {e}")

def split_message(message):
    """Split a message into smaller chunks if it exceeds the maximum length."""
    return [message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]

def escape_markdown(text):
    """Escape special characters for Telegram Markdown."""
    if text is None:
        return "Not Available"
    return re.sub(r'([_*[\]()~`>#+\-=|{}.!])', r'\\\1', str(text))

def format_message(entry):
    """Format a JSON entry into a message for Telegram."""
    return (
        f"🌍 *Source Country:* {escape_markdown(entry.get('source_country'))}\n"
        f"🏛️ *Mission Country:* {escape_markdown(entry.get('mission_country'))}\n"
        f"📄 *Visa Category:* {escape_markdown(entry.get('visa_category'))}\n"
        f"🔖 *Visa Subcategory:* {escape_markdown(entry.get('visa_subcategory'))}\n"
        f"📍 *Center:* {escape_markdown(entry.get('center_name'))}\n"
        f"📅 *Appointment Date:* {escape_markdown(entry.get('appointment_date'))}\n"
        f"👥 *People Looking:* {escape_markdown(entry.get('people_looking'))}\n"
        f"🔗 [Book Now]({escape_markdown(entry.get('book_now_link', 'https://example.com'))})\n"
        f"🕒 *Last Checked:* {escape_markdown(entry.get('last_checked'))}\n"
    )

def fetch_data():
    """Fetch JSON data from the API."""
    url = 'https://vfs.techradiate.com/api/slots'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json',
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()  # Return parsed JSON
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def check_for_updates(json_data):
    """Check for updates in the JSON data for specific countries."""
    global last_sent_data
    updated_entries = []
    for entry in json_data:
        if entry.get('source_country') == 'Angola':
            key = f"{entry.get('source_country', 'Unknown')}->{entry.get('mission_country', 'Unknown')}"
            if key not in last_sent_data or last_sent_data[key] != entry:
                updated_entries.append(entry)
                last_sent_data[key] = entry
    return updated_entries

def main():
    """Main function to fetch data and send updates every 2 minutes."""
    while True:
        json_data = fetch_data()
        if json_data:
            updated_entries = check_for_updates(json_data)
            if updated_entries:
                for entry in updated_entries:
                    message = format_message(entry)
                    message_chunks = split_message(message)
                    for chunk in message_chunks:
                        for chat_id in CHAT_IDS:
                            send_telegram_message(chat_id, chunk)
            else:
                print("No updates detected for Angola.")
        else:
            print("Failed to fetch data.")
        time.sleep(120)

if __name__ == "__main__":
    main()
