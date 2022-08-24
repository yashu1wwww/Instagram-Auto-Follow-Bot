import requests
from datetime import datetime


parameters = {
    "lat": 28.459497,
    "lng": 77.026634,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunset = data["results"]["sunset"]
sunrise = data["results"]["sunrise"]
print(sunset)
print(sunrise)

print()

sunset_hour = sunset.split("T")[1].split(":")[0]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunset_hour)
print(sunrise_hour)

#   UTC TIME TO NORMAL TIME
UTC = 5.3

#   TODO: apply condition if utc + normal = more than 24 then it will be wrong time
print(float(sunset_hour) + UTC)
print(float(sunrise_hour) + UTC)

print()

now = datetime.now()
current_hour = now.hour
print(current_hour)
























