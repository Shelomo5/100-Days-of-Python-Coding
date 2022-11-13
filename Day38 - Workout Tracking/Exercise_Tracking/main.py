import requests
from datetime import datetime
import os

# APP_ID = "15e67e9c"
# import environmental variables for ID and KEY
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
# API_KEY = "b931fcbf97459cc4757e78df95d3c316"

Exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = os.environ["sheety_url"]
GENDER = "male"
WEIGHT = 74.0
HEIGHT = 181.0
AGE = 33

# Prompts user to activity done and for how long or how many Km
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age": AGE
}
# response request made to nutritionix api with headers and parameters above
response = requests.post(url=Exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# Bearer authorization
headers = {
    "Authorization": f"Bearer {os.environ['Token']}"
}

#Time module for current date
today = datetime.now()

# using for loop to iterate through each of the exercise inputs by user
# parameters are Column headers for new row added to google sheet
for exercise in result["exercises"]:
    sheet_param = {
        "workout": {
            "date": today.strftime("%Y%m%d"),
            "time": today.strftime("%X"),
            "exercise": exercise['user_input'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    # Making request for each exercise
    sheet_response = requests.post(url=sheety_url, json=sheet_param, headers=headers)

    print(sheet_response.text)


