import smtplib


sender = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"


def send_mail(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=sender,
            msg=f"Subject:Contact Me\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )