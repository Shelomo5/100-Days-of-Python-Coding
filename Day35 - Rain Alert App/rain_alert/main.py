import requests
# importing Client class for sending sms
from twilio.rest import Client
# import PythonAnywhere class
from twilio.http.http_client import TwilioHttpClient
import os


account_sid = "ACfccfbd14f4195c77954be79c185f1e0d"
auth_token = "a0b044bf0c50855f232d9fb124b981e9"

# API call:https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}
# obtained from API site
api_key = "69f04e4613056b159c2761a9d9e664d2"
OWM_API_Call = "https://api.openweathermap.org/data/2.5/onecall"
Latitude = 46.554649
Longitude = 15.645881

weather_parameters = {
    "lat": Latitude,
    "lon": Longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
# API request
response = requests.get(OWM_API_Call, params=weather_parameters)
# Raise an exception if we don't get 200 response code
response.raise_for_status()
# data in json format stored in a variable
weather_data = response.json()

# obtain only the first 12 hours of data using slicing
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

# set variable to false and switch it to True if it will rain
rain_today = False
# iterates through the 12 hours of weather_slice data
for hour in weather_slice:
    # gets id for each hour
    weather_id = hour["weather"][0]['id']
    # check if id is below 700 indicating rain
    if int(weather_id) < 700:
        rain_today = True

# if true it mean it will rain in next 12 hours
if rain_today:
    # twilio API client needs to be told how to connect to the proxy server
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # code from Twilio to send sms
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain bring an umbrella",
        from_='+19402835625',
        to='+12069475580'
    )
    print(message.status)
