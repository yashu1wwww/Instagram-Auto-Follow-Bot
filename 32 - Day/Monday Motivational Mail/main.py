import datetime as dt
import random
import smtplib


now = dt.datetime.now()
weekday = now.weekday()
sender = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"
receiver = "python.email8050523394@yahoo.com"


if weekday == 1:
    with open("quotes.txt") as file_data:
        data = file_data.readlines()
        quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject:Monday Motivational Quote\n\n{quote}".encode("utf-8")
        )
