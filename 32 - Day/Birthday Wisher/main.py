import pandas
import datetime as dt
from random import randint
import smtplib

#   get today date
now = dt.datetime.now()
today = now.day
sender = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"

#   get birthday person details
data = pandas.read_csv("birthdays.csv")
birthday_person = data[data["day"] == today]
birthday_data = birthday_person.to_dict(orient="records")


if len(birthday_data) > 0:
    if today == birthday_data[0]["day"]:
        for person in birthday_data:
            birthdate = person["day"]
            name = person["name"]
            email = person["email"]

            #   create birthday letter
            with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file_data:
                data = file_data.read()
                letter = data.replace("[NAME]", name)

            #   send birthday mail
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=sender, password=password)
                connection.sendmail(
                    from_addr=sender,
                    to_addrs=email,
                    msg=f"Subject:Birthday Wish\n\n{letter}"
                )
