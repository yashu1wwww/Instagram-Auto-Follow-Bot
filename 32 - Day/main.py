import smtplib

"""
        GMAIL TO YAHOO
"""

sender_mail = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"
receiver_mail = "python.email8050523394@yahoo.com"
message = "Subject:Testing 1\n\nThis is testing email and first mail also"


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=sender_mail, password=password)
    connection.sendmail(
        from_addr=sender_mail,
        to_addrs=receiver_mail,
        msg=message.encode("utf-8")
    )


"""
            YAHOO TO GMAIL


sender_mail = "python.email8050523394@yahoo.com"
password = "8050523394"
receiver_mail = "python.email.8050523394@gmail.com"
message = "Subject:Testing\n\nThis is testing mail"


with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=sender_mail, password=password)
    connection.sendmail(
        from_addr=sender_mail,
        to_addrs=receiver_mail,
        msg=message
    )

"""
