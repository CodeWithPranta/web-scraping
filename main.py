import time
import json
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
print("bcrypt Hashed Password:", bcrypt_hash.decode())

# Simulate CAPTCHA solving with a 2-second delay
print("\nSolving CAPTCHA... (wait 2s)")
time.sleep(2)  # Simulate a 2-second wait for CAPTCHA solving

# Print the fake CAPTCHA token
fake_captcha_token = "0.xaYpEZCxmPN_OkLcH414AXI2yn2SxijvxogjGF53tGRZ1078IJkIpxKQgQ9w-IXM2Eff_vkpaHx6PdeS8Qlu8WjKmXilwzUgwt_ItTSDhDIEUopDFzSVGYMWgNSEElNgjmCNuKw4ywjY298ETVFUJ0Wog3mSwPsQHYwuF1UFcDOnQAR4ElUvtpWNzN_OKOF3Za4tXSlQ66fA-Gh9OUlC1t5cw6-RyjjcMtJORG4oKogUXCcDGq9B4-HqA0UXEMg8JHBAOvpX28KMWo1AtXJaMUJlmXhEcSW0CNg2ecBCGYUEMHS3tBsBHTWWQGwXU8F9DxDIggh9kK-GoEMPp8QCWfZnQkTXpOf_L_ZyGAapdJxMpQQFhHEvMbqEBievjfeJcv_yXBDa675eXf_S_0bUgtwjzmFbH8lVOYzLxg2QuqPdvHY5WjpRtpPbNgJHEPZwd9yjzG18kuMhBY9eLQIUyuuyLxIUz_EB-_e5Vjag9GKAC5Yb-GdKW_9gIPl2TDvu3kQyg2ox5K4zRh7zDqE5jF7lO5WxJIc1dYSHnfZsp4vA5l6zE1A-xlEw4rXFESuydUd1g8g5GREygjBxr0USLLr72OEoXpVlgrMNJ2lOsjguMsGS9YAipLfABCORukjax9FMYeBfnchUPa9jtByzAxi-IU0BaAWpNjwQhcAqxxX_2ixltvEJ26vMbc5xnSnQZ0rBhaDIFjZ5-EKbNvA7UQaLrqx9PBGWCdpA8yalnSZ5Yoyz4-S9B60RjvHrJqos.J49KhTuhykzIJQ99grCqDg.328a3d38dbbe28affd491979b0a291f5ce60e93e1c5efc2477a0bd144dc6aa50"
print(f"Captcha Solved: {fake_captcha_token}")

# Simulate logged-in message
print("\nLogged in successfully. Starting new booking...\n")

# Simulate booking details
application_data = {
    "application_center": "Lithuania Visa Application Center - Baku",
    "appointment_category": "Short Stay",
    "sub_category": "Tourism",
}
print("Application Details:")
print(json.dumps(application_data, indent=4))

# Simulate finding the earliest available slot with 1-second delay per step
print("\nFinding earliest available slot...")
time.sleep(1)
slots = ["06-01-2025", "07-01-2025", "08-01-2025", "09-01-2025", "10-01-2025"]
earliest_slot = min(slots)
print(f"\nEarliest available slot for 1-2 applicants is: {earliest_slot}")

# Simulate applicant details with 1-second delay
print("\nGathering applicant details...")
time.sleep(1)
applicant_details = {
    "first_name": "JONATHAN",
    "last_name": "TROT",
    "gender": "Male",
    "date_of_birth": "15-12-1987",
    "current_nationality": "Azerbaijan",
    "passport": "2222555557785",
    "passport_expiry_date": "13-12-2028",
    "slots": slots,
    "appointment_time": "afternoon, 14:40"
}
print("\nBooking Data:")
print(json.dumps(applicant_details, indent=4))

# Simulate booking confirmation with 1-second delay
print("\nConfirming booking...")
time.sleep(1)
booking_confirmation = {
    "reference": "XYZ29832231246",
    "appointment_type": "standard",
    "date": earliest_slot,
    "time": "14:40-15:00",
    "service_fee": "0.00",
    "additional_fee": "0.00",
    "total": "0.00"
}
print("\nBooking Successful! Details:")
print(json.dumps(booking_confirmation, indent=4))

# Simulate PDF generation and email sending
print("\nPDF has been sent to your login email. 📩")
print("\n🎉 Happy Sticker: Booking Completed Successfully!")
