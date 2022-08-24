import requests


response = requests.get("http://api.open-notify.org/iss-now.json")

# print(response)
# print(response.status_code)
# print(response.json())
# print(response.text)

response.raise_for_status()

print(response.status_code)


data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

print(data)

print(longitude)
print(latitude)

















