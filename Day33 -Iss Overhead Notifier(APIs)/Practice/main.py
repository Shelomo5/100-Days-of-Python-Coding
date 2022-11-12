import requests
# from datetime module import datetime class
from datetime import datetime

MY_LAT = 43.541519
MY_LONG = -1.462680

# # get data from endpoint which is a URL and store it in a response variable
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # exception will be raised if status code isn't 200 meaning our request wasn't successful
# response.raise_for_status()
#
# # retrieving json data
# data = response.json()
#
# # retrieving latitude and longitude
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# # creating tuple
# iss_position = (longitude, latitude)
#
# print(iss_position)

# Dictionary with keys specified in API documentation
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# getting data in response
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

# splitting time to isolate hour value
print(sunrise)
print(sunset)

# getting time now by using now methods
time_now = datetime.now()
# isolate hour value
print(time_now.hour)