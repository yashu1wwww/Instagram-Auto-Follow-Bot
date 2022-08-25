import requests


# "lat": 13.046396,
#     "lon": 77.723328,

API = "6940d199dd16f53e04bbc0f5896b6c44"

parameters = {
    "lat": -12.462320,
    "lon": 130.840942,
    "appid": API,
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()

print(data)

hourly_data = data["hourly"]

b = hourly_data[0]["weather"][0]["id"]

weather_slice = data["hourly"][:12]

