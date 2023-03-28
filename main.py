import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 72.5
HEIGHT_CM = 167.64
AGE = 30


APP_ID = "7d1ea839"
API_KEY = "588dd9e42c1657049bf9bc2761bdfcc9"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = 'https://api.sheety.co/d886ea813f3619317363aeb768f6a88b/myWorkouts/workouts'

exercise_input = input("Tell which exercise you did today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}




# "query": "ran 3 miles"
response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)
# run 3K and walk 3 miles

today_date = datetime.now().strftime("%m%d%Y")
now_time = datetime.now().strftime("%X")


bearer_header = {
    "Authorization":  "Bearer stom327"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers= bearer_header)

print(sheet_response.text)