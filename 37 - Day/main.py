import requests
from datetime import datetime


CREATE_USER_END_POINT = "https://pixe.la/v1/users"
USERNAME = "kingarunesh"
TOKEN = "thisisaruneshtoken"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


#   create new user
# response = requests.post(url=CREATE_USER_END_POINT, json=parameters)
# print(response.text)


#   create new graph
GRAPH_END_POINT = f"{CREATE_USER_END_POINT}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

TOKEN_HEADER = {
    "X-USER-TOKEN": TOKEN
}

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url=GRAPH_END_POINT, headers=TOKEN_HEADER, json=graph_parameter)
# print(response.text)


#   new value in graph
NEW_PIXEL_GRAPH = f"{CREATE_USER_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=9, day=28)

new_pixel_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "17.0"
}

# response = requests.post(url=NEW_PIXEL_GRAPH, headers=TOKEN_HEADER, json=new_pixel_parameter)
#
# print(response.text)


#   update pixel
UPDATE_ENDPOINT = f"{CREATE_USER_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/20220928"
update_parameter = {
    "quantity": "1.1"
}

# response = requests.put(url=UPDATE_ENDPOINT, headers=TOKEN_HEADER, json=update_parameter)
# print(response.text)


#   DELETE PIXEL
delete_endpoint = f"{CREATE_USER_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/20220928"

response = requests.delete(url=delete_endpoint, headers=TOKEN_HEADER)

print(response.text)














