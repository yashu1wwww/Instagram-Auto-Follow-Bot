import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime


APP_ID = "1c80b133"
API_KEY = "cd60d858ca91fd0fef4661298b8719bc"
GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 157
AGE = 23
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(END_POINT, json=parameters, headers=header)

results = response.json()["exercises"]


#   SHEET
sheet_endpoint = "https://api.sheety.co/3c03c541e1419207043b0bd54b40c679/myWorkouts/workouts"

header_sheet = {
    "Content-Type": "application/json"
}

basic = HTTPBasicAuth("kingarunesh", "8050523394")


for result in results:
    print(result)

    body_sheet = {
        "workout": {
            "date": datetime.now().strftime("%Y%m%d"),
            "time": datetime.now().strftime("%X"),
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=body_sheet, auth=basic)

    print(sheet_response.json())

















