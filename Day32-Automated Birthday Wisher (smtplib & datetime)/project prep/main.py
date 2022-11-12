# import smtplib
#
# my_email =
# password =
#
# # Creating object from SMTP class, location of email provider SMTP server  provided
# # Make sure to modify security settings from the account you're sending from
# # lookup email server url for specific email host yahoo, gmail, ect...
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # secures connection to email server
#     connection.starttls()
#     # loging in
#     connection.login(user= my_email, password=password)
#     # sends mail
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=,
#                         msg="Subject:Hello\n\nThis is the body of my email ")

# import datetime as dt
# # access datetime class from datetime module(dt) and applying now method to get current datetime object
# now = dt.datetime.now()
# # using now object to return current year, month, and day of week as a number
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# # creating datetime object
# date_of_birth = dt.datetime(year=1989, month=2, day=5)
# print(date_of_birth)

import smtplib
import datetime as dt
import pandas
import random
import os

my_email = os.environ["my_email"]
password = os.environ["password"]

# access datetime class from datetime module(dt) and applying now method to get current datetime object
now = dt.datetime.now()
# using now object to return current year, month, and day of week as a number
year = now.year
month = now.month
day_of_week = now.weekday()
if day_of_week == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        today_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Quote\n\n{today_quote}")


