from DrissionPage import Chromium
import time
import json

tab = Chromium().latest_tab
# Navigated to the ivac page
tab.get("https://payment.ivacbd.com/")
load = tab.wait.ele_displayed('#emergencyNoticeCloseBtn')

if load:
    notice_btn = tab.ele('#emergencyNoticeCloseBtn')
    # Close notice board
    notice_btn.click()
    print('Notice board closed!')
else:
    print('Notice board not found!')

# Info from a json file
with open('ivac_data.json', 'r') as f:
    # Load the JSON data into python dictionary
    data = json.load(f)

# Run the bot for specific user 
# Change this line before run this script according to user data
user = data['user_1']

# Application info
high_commission = tab.ele('#highcom')
high_commission.click()

if user['highcom'] == 'Dhaka':
    highcom = tab.ele('@label=Dhaka')
elif user['highcom'] == 'Chittagong':
    highcom = tab.ele('@label=Chittagong')
elif user['highcom'] == 'Rajshahi':
    highcom = tab.ele('@label=Rajshahi')
elif user['highcom'] == 'Khulna':
    highcom = tab.ele('@label=Khulna')
else:
    print("High commission name not found!")

highcom.click()

web_id = tab.ele('@name=web_id')
web_id.input(user['web_file_number'])
web_id_repeat = tab.ele('@name=web_id_repeat')
web_id_repeat.input(user['web_file_number'])

# IVAC center 
ivac_center = tab.ele('#ivac')
ivac_center.click()

ivac_center_set = {
    '@label=IVAC, BARISAL', 
    '@label=IVAC, JESSORE', 
    '@label=IVAC, Dhaka (JFP)', 
    '@label=IVAC, SATKHIRA',
    '@label=IVAC, CHITTAGONG',
    '@label=IVAC, CUMILLA',
    '@label=IVAC, NOAKHALI',
    '@label=IVAC, BRAHMANBARIA',
    '@label=IVAC , RAJSHAHI',
    '@label=IVAC, RANGPUR',
    '@label=IVAC, THAKURGAON',
    '@label=IVAC, BOGURA',
    '@label=IVAC, KUSHTIA',
    '@label=IVAC, SYLHET',
    '@label=IVAC, MYMENSINGH',
    '@label=IVAC, KHULNA'
    }

for ivac_center in ivac_center_set:
    if user['ivac_center'] == ivac_center:
        center = tab.ele(ivac_center)
        center.click()

# Visa type field
ivac_visa_type = tab.ele('#ivac_visa_type')
ivac_visa_type.click()

if user['visa_type'] == 'TOURIST VISA':
    visa_type = tab.ele('@label=TOURIST VISA')
elif user['visa_type'] == 'MEDICAL/MEDICAL ATTENDANT VISA':
    visa_type = tab.ele('@label=MEDICAL/MEDICAL ATTENDANT VISA')
elif user['visa_type'] == 'BUSINESS VISA':
    visa_type = tab.ele('@label=BUSINESS VISA')
elif user['visa_type'] == 'ENTRY VISA':
    visa_type = tab.ele('@label=ENTRY VISA')
elif user['visa_type'] == 'STUDENT VISA':
    visa_type = tab.ele('label=STUDENT VISA')
else:
    print('Visa type not found!')

visa_type.click()

time.sleep(1)
save_next_btn = tab.ele('Save and Next')
save_next_btn.click()

# 2nd page automation
load_personal_info_fields = tab.wait.ele_displayed('@name=name')
if load_personal_info_fields:
    name = tab.ele('@name=name')
    name.input(user['name'])
else:
    print('Overview fields are not properly!')

email = tab.ele('@name=email')
email.input(user['email'])
phone = tab.ele('@name=phone')
phone.input(user['phone'])

# Find the Save and show overview btn
save_show_overview_btn = tab.ele('Save and show overview')
save_show_overview_btn.click()

# Toss agreement
agreement_checkbox = tab.wait.ele_displayed('#tos_agree')
if agreement_checkbox:
    tos = tab.ele('#tos_agree')
    tos.click()

move_for_pay_btn = tab.ele('Confirm and move for payment')
move_for_pay_btn.click()









