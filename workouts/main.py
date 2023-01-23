import requests
from datetime import datetime
import os 
NUTRITION_API_ID = "519a1c9f"
NUTRITION_API_KEY = "3f49aa609d0d7095ce0d7734a6a2228d"

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {
 "query":input("What is your exercise?"),
 "gender":"male",
 "weight_kg":81,
 "height_cm":180,
 "age":34
}
user_headers = {
    "x-app-id" : os.environ["NUTRITION_API_ID"],
    "x-app-key" : os.environ["NUTRITION_API_KEY"],
    "Content-Type":"application/json"
}

response = requests.post(url=api_endpoint, json=parameters, headers=user_headers)



sheety_api = "https://api.sheety.co/7872c97407a0076c76f4609dab8f419f/myWorkouts/workouts"
sheety_params = {
    "workout" : {
        "date" : datetime.today().strftime("%d/%m/%Y"),
        "time" : datetime.today().strftime("%H:%M:%S"),
        "exercise" : response.json()["exercises"][0]["user_input"].title(),
        "duration" : response.json()["exercises"][0]["duration_min"],
        "calories" : response.json()["exercises"][0]["nf_calories"]
    }
}

sheety_headers = {
    "Authorization" : os.environ["SHEETY_AUTHORIZATION"],
    "Content-Type":"application/json"
}

sheety_response = requests.post(url=sheety_api, json=sheety_params, headers=sheety_headers)
# print(sheety_response.text)

