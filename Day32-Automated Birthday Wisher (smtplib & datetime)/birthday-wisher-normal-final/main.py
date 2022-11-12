##################### Normal Starting Project ######################
import smtplib
# from datetime module import datetime class
from datetime import datetime
import pandas
import random
import os

my_email = os.environ["my_email"]
password = os.environ["password"]


# access datetime class to create datetime object
now = datetime.now()
month = now.month
day = now.day

# tuple of today's month and day
today_tuple = now.month, now.day

# converting csv into df
bdata = pandas.read_csv("birthdays.csv")

# using dictionary comprehension to create dictionary where month and day are the key values for each rows
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in bdata.iterrows()}

# if today tuple matches a date in bday dict.
if today_tuple in birthdays_dict:
    # get item/ data row in dictionary where key matches today_tuple
    birthday_row = birthdays_dict[today_tuple]
    # file path to one of 3 three letters chosen randomly
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # opening file
    with open(file_path) as letter:
        # read file
        contents = letter.read()
        # replace actual name of person in the row of dictionary and place it in letter
        letter = contents.replace("[NAME]", birthday_row["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # sending email
        connection.sendmail(
            from_addr=my_email,
            # email address of bday person
            to_addrs=birthday_row["email"],
            msg=f"Subject:Happy Bday\n\n{letter}")

