import requests
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

user_params = {
    "query": "run 5km and cycled 10 minutes",
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 25
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    json=user_params,
    headers=nutritionix_headers
)
result = response.json()

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"])
        }
    }

    sheety_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=sheet_input,
        headers={"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"}
    )

    print(sheety_response.text)
