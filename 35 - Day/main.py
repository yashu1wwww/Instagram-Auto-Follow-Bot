import requests


"""
        GET RESPONSE BY CITY NAME

API = "1f6f52fb87ecdd92ca2b73dd3739879d"

PARAMETERS = {
    "q": "delhi",
    "appid": API
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather", params=PARAMETERS)
response.raise_for_status()
print(response.json())
"""

API = "6940d199dd16f53e04bbc0f5896b6c44"


PARAMETER = {
    "lat": 14.442599,
    "lon": 79.986458,
    "appid": API,
    "exclude": "current,minutely,daily"
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=PARAMETER)

response.raise_for_status()

data = response.json()

print(data)

#   1 - method
hourly = data["hourly"]
will_rain = False

for i in range(0, 12):
    id = hourly[i]["weather"][0]["id"]
    if id < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella")



# #   2 - method
# hourly = data["hourly"][:12]
#
# will_rain = False
#
# for hourly_data in hourly:
#     ids = hourly_data["weather"][0]["id"]
#     if ids < 700:
#         will_rain = True
#
#
# if will_rain:
#     print("Bring Umbrella")




















