import requests
from twilio.rest import Client
import os


#   twilio
account_sid = "AC12407e5ef62b6460df405419a923da86"
auth_token = "224353f389ef7a129780136a7d60035f"
client = Client(account_sid, auth_token)

parameters = {
    "lat": 21.145800,
    "lon": 79.088158,
    "appid": "495cafef559813c110a7a061433dd9df",
    "exclude": "current,minutely,daily"
}
endpoint_url = "https://api.openweathermap.org/data/2.8/onecall"

response = requests.get(url=endpoint_url, params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
hourly = data["hourly"][:12]
rain = False


for hour in hourly:
    if hour["weather"][0]["id"] < 700:
        rain = True


if rain:
    message = client.messages \
        .create(
        body="Bring an Umbrella",
        from_="+12058434651",
        to="+91 89718 18410"
    )

    print(message.status)



































