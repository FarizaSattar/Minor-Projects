from datetime import datetime
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# ------------------- CONFIGURATION -------------------

MY_EMAIL = "your_email@example.com"  # Replace with your email
MY_PASSWORD = "your_email_password"  # Replace with your email password
SMTP_SERVER = "smtp.example.com"     # Replace with your SMTP server address

# Prompt the user for their name
sender_name = input("Enter your name: ")

# ------------------- LOAD AND CHECK BIRTHDAYS -------------------

today = datetime.now()
today_date = (today.month, today.day)

# Load birthdays from CSV
data = pd.read_csv("birthdays.csv")

# Create a dictionary with (month, day) as keys
birthdays = {(row["month"], row["day"]): row for _, row in data.iterrows()}

# ------------------- SEND EMAIL IF MATCH FOUND -------------------

if today_date in birthdays:
    person = birthdays[today_date]

    # Pick a random birthday letter template
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as file:
        message = file.read().replace("[BIRTHDAY_PERSON_NAME]", person["full_name"]).replace("[SENDER_NAME]", sender_name)

    # Create the email message
    msg = MIMEText(message, 'plain')
    msg['Subject'] = 'Happy Birthday!'
    msg['From'] = formataddr((sender_name, MY_EMAIL))
    msg['To'] = person["email"]

    # Send the birthday email
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, person["email"], msg.as_string())

    print(f"Birthday email sent to {person['full_name']} at {person['email']}.")
else:
    print("No birthdays today.")
