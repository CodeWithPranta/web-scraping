import requests

# Create a session object to manage cookies and session state
session = requests.Session()

# Define your headers with the required cookies (from your logged-in browser)
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,bn;q=0.8",
    "cache-control": "no-cache",
    "cookie": "_ga=GA1.1.1826811776.1734607514; __gads=ID=15e0cabd83f0536b:T=1734607514:RT=1734750157:S=ALNI_MaTvtLkkJZImLdFb6VuzhMnJrHmRw; __gpi=UID=00000face72d2714:T=1734607514:RT=1734750157:S=ALNI_MZ5Jfy-uFM4HEowMW_4DNllOq6Vmg; __eoi=ID=db0aead2538b087e:T=1734607514:RT=1734750157:S=AA-AfjbZoAoSZ7VFv4GlVGAWyzXx; io=eWObIkUWXBLNlnuuAKOs; FCNEC=%5B%5B%22AKsRol8P-UmcBKTJ5C-GXcPjJk1XBwReL67fvhTQpFujjNEpvSy26XYTWYoTjCb0g5p5WxmeyvUneaOklsKhxTDLsYzUq-Okfcjloi_SKkEn_5FMYNrth0S0Ka54whiRQ_9Te2ab8utxIgJkfbsGRN2ynhqKqXYbiA%3D%3D%22%5D%5D; _ga_90GRT6N40B=GS1.1.1734750160.3.1.1734750325.0.0.0; express:sess=eyJmbGFzaCI6eyJzdWNjZXNzIjpbIllvdSBsb2dnZWQgaW50byBhIHNlY3VyZSBhcmVhISJdfSwidXNlcm5hbWUiOiJwcmFjdGljZSJ9; express:sess.sig=QB6LD3-oqKp5QNfuN66ceVwVu0M",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://practice.expandtesting.com/login",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
}

# Set headers in the session
session.headers.update(headers)

# URL of the page to scrape after logging in
url = 'https://practice.expandtesting.com/secure'

# Use the session to get the secure page
response = session.get(url)

# Set the encoding and print the HTML content
html = response.text
print(html)
