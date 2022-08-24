import smtplib


sender_mail = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"
receiver_mail = "python.email8050523394@yahoo.com"
message = "Subject:ISS\n\nLook up to SKY"


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_mail, password=password)
        connection.sendmail(
            from_addr=sender_mail,
            to_addrs=receiver_mail,
            msg=message.encode("utf-8")
        )
