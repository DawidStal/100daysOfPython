import datetime as dt
import random
import os
import pandas
import smtplib

birthdays_csv = pandas.read_csv("Day-32-Birthday-Wisher\\birthdays.csv")
now = dt.datetime.now()
today = (now.day, now.month)
birthdays = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in birthdays_csv.iterrows()}

# Check if today matches a birthday in the birthdays.csv
if today in birthdays:
    person = birthdays[today]
    # Pick a random letter
    letter_choice = random.choice(os.listdir("Day-32-Birthday-Wisher\\letter_templates"))
    # Get content of the letter
    with open(f"Day-32-Birthday-Wisher\\letter_templates\\{letter_choice}", "r") as letter:
        letter_content = letter.read()
    # Replace [Name] with the name of the person
    message = letter_content.replace("[NAME]", person["name"])

    # Send email
    sender_email = "" # set sender email here
    password = "" # set sender password here
    to_email = person["email"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=to_email, msg=f"Subject:Happy Birthday\n\n{message}")
