import pandas
import datetime as dt
from random import randint
import smtplib


#   get today date
now = dt.datetime.now()
current_day_month = (now.day, now.month)

#   login - email & password
sender = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"

#   get birthday person details
data = pandas.read_csv("birthdays.csv")

data_dict = data.to_dict(orient="records")
# print(data_dict)

for item in data_dict:
    birth_day_month = (item["day"], item["month"])
    if current_day_month == birth_day_month:
        name = item["name"]
        email = item["email"]

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
