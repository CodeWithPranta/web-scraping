import requests
from twocaptcha import TwoCaptcha
import bcrypt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode

# RSA public key (already in PEM format)
public_key_pem = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpigN3/5Ti/WJk51pbPQdpCe96
TPVoeMAk/cUlAPpYh8zGpr6zssbM11Je1SoQTiuipxIL+c0oGXti8vLzln3yfS+N
56wuSh0Hyt1Z+waSx6IDFlfzImEtq8m1osS32B83HRiFZbeKB8QIRJhZil1pJSzM
sg0Y0QmDyv1yR4FzIQIDAQAB
-----END PUBLIC KEY-----"""

# Example password 
password = 'Web#140248est'
  
# Convert password to bytes
password_bytes = password.encode('utf-8') 

# Encrypt the password using RSA public key
def encrypt_password_with_rsa(password_bytes, public_key_pem):
    key = RSA.import_key(public_key_pem)
    cipher = PKCS1_OAEP.new(key)
    encrypted_password = cipher.encrypt(password_bytes)
    return b64encode(encrypted_password).decode('utf-8')

# Encrypt the password
encrypted_password = encrypt_password_with_rsa(password_bytes, public_key_pem)
print("Encrypted Password:", encrypted_password)

# Hashing the password using bcrypt (optional, based on your original code)
salt = bcrypt.gensalt()
bcrypt_hash = bcrypt.hashpw(password_bytes, salt)
print("bcrypt Hashed Password:", bcrypt_hash)

# Initialize the TwoCaptcha solver with your API key
solver = TwoCaptcha('4305c761c3ec186e3acef079df72463c')

# Attempt to solve CAPTCHA
try:
    result = solver.turnstile(
        sitekey='0x4AAAAAAACYaM3U_Dz-4DN1',
        url='visa.vfsglobal.com/aze/en/ltu/login',
    )
    # Ensure the CAPTCHA solve result contains a token
    if 'code' in result:
        captcha_token = result['code']
        print("CAPTCHA Solved Successfully! Token:", captcha_token)
    else:
        print("CAPTCHA solving failed. Response:", result)
        exit()  # Exit the script if CAPTCHA solving fails
except Exception as e:
    print("Error solving CAPTCHA:", str(e))
    exit()  # Exit the script if an exception occurs

# Proxy API endpoint
# proxy_url = "https://proxy.scrapeops.io/v1/"
# proxy_params = {
#     'api_key': '9913642a-f917-42bc-bc9f-814b44438fa6',
#     'url': 'https://lift-api.vfsglobal.com/user/login',
# }

# Login URL
#login_url = proxy_url

login_url = 'https://lift-api.vfsglobal.com/user/login'

# Login data (include the solved CAPTCHA token and encrypted password)
credentials = {
    'username': 'codewithpranta@gmail.com',
    'password': encrypted_password,  # Use encrypted password
    'missioncode': 'ltp',
    'countrycode': 'npl',
    'languageCode': 'en-US',
    'captcha_version': 'cloudflare-v1',
    'captcha_api_key': captcha_token,  # Pass the CAPTCHA token here
    'cf-turnstile-response': captcha_token,  # Include the hidden token
}

# Headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,bn;q=0.8",
    "cache-control": "no-cache",
    "clientsource": "MaqiVlL/EgJZaFsE0ISbLlDTvdeYLOWaMevRp7ETD3NAR3R4SyEVj2evBJ7DSru2/akcn9dKYSifLUTRoUl50jZl+bzaEc07RJ7hTGkGhvNeZG+2pM2m6mu7Vo9oCnSnW337EcxzGOZhny9Jrrmi2qZozSpofd8Wfsdx9cYaWcI=",
    "content-length": "1203",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://visa.vfsglobal.com",
    "pragma": "no-cache",
    "referer": "https://visa.vfsglobal.com/",
    "route": "npl/en/ltp",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
}

# Make the POST request using ScrapeOps proxy
response = requests.post(
    url=login_url,
    # params=proxy_params,
    headers=headers,
    data=credentials
)

# Print the response status code
print("Response Status Code:", response.status_code)

# Print the response body for more information
print("Response Body:", response.text)

# Additional information to get more context on the error
if response.status_code != 200:
    print("Response Headers:", response.headers)
    print("Response Cookies:", response.cookies)
    print("Response Content-Type:", response.headers.get('Content-Type'))

    # If the response is in JSON format, try to parse it and print any error message
    try:
        response_json = response.json()
        print("Response JSON:", response_json)
    except ValueError:
        print("Response is not in JSON format.")
    
    # If there's a specific error code or message in the response, log it
    if 'error' in response.text.lower():
        print("Error in response body:", response.text)
else:
    print("Request successful, no errors encountered.")
