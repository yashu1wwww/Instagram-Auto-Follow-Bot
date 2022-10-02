import smtplib
import requests
from bs4 import BeautifulSoup
import lxml


#   requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

END_POINT = "https://www.amazon.com/dp/B0B5QC91RV/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
response = requests.get(url=END_POINT, headers=headers)
data = response.text


#   scraping
soup = BeautifulSoup(data, "lxml")
title = soup.find(name="span", id="productTitle").getText().strip()
product_price = soup.find(name="span", class_="a-offscreen").getText()
price = float(product_price.split("$")[1])


#   smtp
sender_email = "python.email.8050523394@gmail.com"
password = "ocvsredwlcdumipb"

message = f"Subject:Amazon Price Alert\n\n{title}\nis now at {price}\n{END_POINT}".encode("utf-8")

if price < 150:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=sender_email, msg=message)

    print("Alert sent")
