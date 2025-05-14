import RPi.GPIO as GPIO
import time
import requests
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

# Google Sheets Web App URL
WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbzFmUQHW-7cAtuAGsJ0_lBs62K6hZpSDpwaUB4V3cQ4HEg1H7fqTkaOL-RFrDRbcHQk/exec'



GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
reader = SimpleMFRC522()

try:
    while True:
        print("Place your card...")
        id, text = reader.read()
        cleaned_text = text.strip().upper()
        print("ID:", id)
        print("Text:", cleaned_text)

        if id == 782698349564 and cleaned_text == 'NIRU':
            team_name = 'TEAM B8'
            access_status = 'Access Granted'
            GPIO.output(40, 1)
        else:
            team_name = cleaned_text
            access_status = 'Access Denied'
            GPIO.output(40, 0)

        payload = {
            'rfid_id': str(id),
            'team_name': team_name,
            'access_status': access_status
        }

        response = requests.post(WEBHOOK_URL, json=payload)
        print("Sent to Google Sheets:", response.text)

        time.sleep(5)
        GPIO.output(40, 0)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
