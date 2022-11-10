import requests
from datetime import datetime
import smtplib
import time
# current location
MY_LAT = 43.541519 # Your latitude
MY_LONG = -1.462680 # Your longitude

my_email = "cantshlomedown@gmail.com"
password = "xfyfonyakazzaace"

# function returns true if International Space Station is overhead
def position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # check to see if iss position is close to current location
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    # getting sunrise and sunset time at current location
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # getting current time in hour
    time_now = datetime.now()
    hour = time_now.hour
    # returns true when it's dark
    if hour <= sunrise or hour >= sunset:
        return True

while True:
    # code executes every 60 seconds
    time.sleep(60)
    # send email if iss position is overhead and it's night time
    if position() and night_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            # sending email to myself
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Lookup ISS is overhead \n\n Look above")