import os
import csv
import smtplib
import pandas as pd
from email.message import EmailMessage

# Get email and password from env
EMAIL_ADDRESS = os.environ.get("TEST_EMAIL")
EMAIL_PASSWORD = os.environ.get("TEST_PASS")

# Pandas

df = pd.read_csv("dwc.csv")
emails = df["Email"]
email_list = list(emails)
print(email_list)

# Create email

msg = EmailMessage()
msg["Subject"] = "Test Drive this weekend"
msg["From"] = EMAIL_ADDRESS
msg["To"] = email_list
msg.set_content("Hello, The car is ready for a test drive whenever you are.")


# Logic

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
