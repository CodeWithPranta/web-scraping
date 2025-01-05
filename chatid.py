import requests

BOT_TOKEN = "7414817026:AAGavLA5stpYOvRUQWg5grxSy2nXwK4ssgE"  # Replace with your bot token
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(URL)
data = response.json()

# Print the Chat ID and the message details
print(data)
