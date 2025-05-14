
response = requests.post(WEBHOOK_URL, json=payload)
        print("Sent to Google Sheets:", response.text)

        time.sleep(5)
        GPIO.output(40, 0)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
