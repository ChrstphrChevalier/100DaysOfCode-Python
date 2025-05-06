from smtplib import *
from email.message import EmailMessage
from datetime import datetime as dt
import pandas as pd
import random

my_email = '[YOUR EMAIL]@gmail.com'
password = '[YOUR PASSWORD Of APPLICATION]'

today = [dt.now().day, dt.now().month, dt.now().year]
try:
    data = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    print("ERROR ❌ : no data files found")
    exit()

def is_birthday():
    matching_rows = pd.DataFrame()
    if today[0] in data['day'].values:
        matching_rows = data[data['day'] == today[0]]
        if today[1] in matching_rows['month'].values:
            matching_rows = matching_rows[matching_rows['month'] == today[1]]
            for i, row in matching_rows.iterrows():
                file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
                try:
                    with open(file_path, 'r') as letter:
                        content = letter.read()
                        content = content.replace("[NAME]", row['name'])
                        matching_rows.at[i, 'letter'] = content
                except FileNotFoundError:
                    print(f"ERROR ❌: Letter template not found for {row['name']}")
                    matching_rows.at[i, 'letter'] = "No letter available."
    return matching_rows

def birthday_wisher():
    data = is_birthday()

    for _, row in data.iterrows():
        if 'letter' in row:
            msg = EmailMessage()
            msg['Subject'] = "Happy Birthday ! 🎉"
            msg['From'] = my_email
            msg['To'] = row['email']
            msg.set_content(row['letter'])

            try:
                with SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.send_message(msg)
                    print(f"Email sent to {row['name']} ({row['email']})")
            except Exception as e:
                print(f"ERROR ❌: Failed to send email to {row['name']} ({row['email']}) due to {e}")

while True:
    birthday_wisher()