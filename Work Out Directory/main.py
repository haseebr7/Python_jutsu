import requests
from datetime import *
import os

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 185
AGE = 20

# -------
USERNAME = os.getenv("USERNAME")
PASSWORD =  os.getenv("PASSWORD")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
# -------

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

current_date = "2025/10/13"   #datetime.now().strftime("%Y/%m/%d")
current_time = datetime.now().strftime("%X")
# --------------------------

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response =  requests.post(EXERCISE_ENDPOINT, json=parameters, headers= headers)
result = response.json()
print(result)

for i in result["exercises"]:


    exercise = {
        "sheet1": {
        "date": current_date,
        "time": current_time,
        "exercise": i["name"].title(),
        "duration": i["duration_min"],
        "calories": i["nf_calories"]
    }
}


    response = requests.post(SHEETY_ENDPOINT, json=exercise, auth=(USERNAME,PASSWORD))
    respond = response.json()

    print(respond)
