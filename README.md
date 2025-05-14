# RFID-Access-Control
Raspberry Pi RFID-based Access Control System with Google Sheets integration

RFID Access Control System

This project uses an RFID module and Raspberry Pi to log access control to Google Sheets via a Webhook.

## Hardware:
- Raspberry Pi
- MFRC522 RFID Reader
- RFID Tags
- LED or Door Lock (connected to GPIO 40)

## Features:
- RFID Authentication
- Access logging to Google Sheets
- LED output for access status

## Dependencies:
- `RPi.GPIO`
- `mfrc522`
- `requests`
