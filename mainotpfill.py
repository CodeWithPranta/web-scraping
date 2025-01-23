from DrissionPage import ChromiumOptions, Chromium
import time
import json
import firebase_admin
from firebase_admin import credentials, db
import re
import datetime

# ✅ Step 1: Initialize Firebase with Service Account Key
cred = credentials.Certificate("C:\\Users\\ebask\\Desktop\\VisasBot3\\serviceAccountKey.json")  # Replace with your file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://readotp-c0a79-default-rtdb.firebaseio.com/'  # Replace with your database URL
})


# 📌 **Function to Fetch the Latest OTP from Firebase with Timestamp Check**
def get_latest_otp():
    max_age = 180  # OTP'nin maksimum süresi 180 saniye (3 dakika)

    while True:  # Eğer eski OTP varsa 5 saniye bekleyip tekrar dener.
        ref = db.reference('sms_messages')  # Reference to the "sms_messages" node
        data = ref.get()

        if not data:
            print("❌ No SMS data found in Firebase!")
            return None

        last_key = max(data.keys())  # Get the latest entry
        last_sms = data[last_key]

        # ✅ Timestamp bilgisini al ve saniyeye çevir (milisaniyeden saniyeye dönüştürme)
        timestamp_ms = last_sms.get('timestamp', 0)  # Eğer timestamp yoksa 0 döner
        timestamp_sec = int(timestamp_ms / 1000)  # Milisaniyeyi saniyeye çevir
        current_time = int(time.time())  # Şu anki zaman (saniye cinsinden)

        # ✅ OTP'nin yaşı hesaplanır
        otp_age = current_time - timestamp_sec

        print(f"\n📩 Latest SMS: {last_sms['message']}")
        print(f"⏳ OTP Age: {otp_age} seconds (Max allowed: {max_age} seconds)")

        if otp_age > max_age:
            print("⚠️ OTP is too old! Waiting for a new message...")
            time.sleep(30)  # 5 saniye bekle ve tekrar dene
            continue  # Döngü başa dönsün, yeni OTP almayı denesin
        
        # ✅ OTP içindeki 6 haneli kodu ayıkla
        match = re.search(r'\b\d{6}\b', last_sms['message'])  
        if match:
            otp = match.group()
            print(f"✅ Extracted OTP: {otp}")
            return otp
        else:
            print("❌ No OTP found in the message!")
            return None
    
    # 📌 **Function to Convert OTP into Virtual Keyboard Input Format**
def otp_to_keys(otp):
    return [f"@name={digit}" for digit in otp]  # Convert each digit to virtual keyboard key format

# 📌 **Mitmproxy Proxy Ayarları (Unchanged)**
proxy_host = "127.0.0.1"
proxy_port = "8080"

# **DrissionPage için Proxy Ayarları (Unchanged)**
options = ChromiumOptions()
options.set_proxy(f"{proxy_host}:{proxy_port}")  
options.set_argument('--ignore-certificate-errors')  

# **Initialize Chromium Browser (Unchanged)**
browser = Chromium(options)
tab = browser.new_tab()  # ✅ Your preferred method

# **Navigate to the login page (Unchanged)**
tab.get('https://visa.vfsglobal.com/tur/en/aut/login')
print("✅ Navigated to login page.")

time.sleep(2)  # Allow time for page to load

# **Cookies Management (Unchanged)**
accept_cookies = tab.ele('#onetrust-accept-btn-handler', timeout=10)
if accept_cookies:
    accept_cookies.click()
    print("✅ Cookies accepted.")
else:
    print("⚠️ Cookies already accepted.")

# **Fill Email (Unchanged)**
email_field = tab.ele('#email', timeout=5)
if email_field:
    email_field.input('birvize5467423143@gmail.com')
    print("✅ Email field filled.")
else:
    print("⚠️ Email field not found!")

time.sleep(3)

# **Locate and Click Password Field (Unchanged)**
password_field = tab.ele('#mat-input-4', timeout=10)
if password_field:
    password_field.click()
    print("✅ Password field clicked.")
    
    time.sleep(1)

  
    # **Enter Password via Virtual Keyboard (Unchanged)**
    keys = ["@name={shift}", "@name=H", "@name={shift}", "@name=a", "@name=c", "@name=e", "@name=t", 
            "@name=t", "@name=e", "@name=p", "@name=e", "123", "@name=0", "@name=6", "@name={symbolic}" , "@name=*"]


    for key in keys:
        key_element = tab.ele(key, timeout=5)
        if key_element:
            key_element.click()
            time.sleep(0.5)
        else:
            print(f"⚠️ Key {key} not found!")

    # **Click 'Sign In' Button (Unchanged)**
    sign_in_button = tab.ele('Sign in', timeout=10)
    if sign_in_button:
        sign_in_button.click()
        print("✅ Password entered and sign-in clicked.")
    else:
        print("⚠️ 'Sign in' button not found!")

else:
    print("⚠️ Password field not found.")

time.sleep(2)

# **Click Login Button (Unchanged)**
login_button = tab.ele('Sign In', timeout=10)
if login_button:
    login_button.click()
    print("✅ Login button clicked.")
else:
    print("⚠️ Login button not found.")

time.sleep(40)

otp_code = get_latest_otp()

if otp_code:
    # **Enter OTP in the Input Field**
    otp_input = tab.ele('#mat-input-5', timeout=10)  # Replace with actual OTP field selector
    if otp_input:
        otp_input.click()
        print("✅ OTP input field clicked.")

        # 📌 **Generate Virtual Keyboard Keys for OTP**
        otp_keys = otp_to_keys(otp_code)

        print(f"✅ OTP Keys to be entered: {otp_keys}")

        # 📌 **Enter OTP via Virtual Keyboard**
        for key in otp_keys:
            key_element = tab.ele(key, timeout=5)
            if key_element:
                key_element.click()
                time.sleep(0.5)  # Simulate typing delay
            else:
                print(f"⚠️ Key {key} not found!")

        print("✅ OTP entered via virtual keyboard.")


       # **Click 'Sign In' Button (Unchanged)**
        otp_enter = tab.ele("@name={enter}", timeout=10)
        sign_in_button = tab.ele('Sign In', timeout=10)

        if otp_enter:
            otp_enter.click()
            print("✅ Password entered and enter clicked.")
            
            if sign_in_button:
                sign_in_button.click()
                print("✅ Password entered and sign-in clicked.")
            else:
                print("⚠️ 'Sign in' button not found!")
        else:
            print("⚠️ OTP input field not found!")

else:
    print("❌ No OTP available from Firebase!")




# **Capture Updated Cookies After Login**
tab.wait.load_start()  
cookies = tab.cookies()
print("🔹 Updated Cookies:", cookies)

# **Save Cookies to a File for Future Requests**
with open("cookies.json", "w", encoding="utf-8") as file:
    json.dump(cookies, file, indent=4)
print("✅ Cookies saved to cookies.json")

# **Final Step: Browser Cleanup (Optional)**
time.sleep(50)
## tab.close()
