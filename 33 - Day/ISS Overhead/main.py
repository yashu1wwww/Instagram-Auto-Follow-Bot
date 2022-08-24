import requests
from datetime import datetime
from config import send_mail
from time import sleep


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_longitude)
print(iss_latitude)


# Your position is within +5 or -5 degrees of the ISS position.

# MY_LAT = 28.704060
# MY_LONG = 77.102493
MY_LAT = -51.2553
MY_LONG = 121.4025

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now().hour

# If the ISS is close to my current position
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    # and it is currently dark
    if time_now >= sunrise or time_now <= sunset:
        # Then send me an email to tell me to look up.
        send_mail()
        print("Mail Sent")
# BONUS: run the code every 60 seconds.
