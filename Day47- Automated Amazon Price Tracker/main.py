import requests
from bs4 import BeautifulSoup
import smtplib
import os
import lxml

my_email = os.environ["my_email"]
password = os.environ["password"]

# URL of product we're tracking
amazon_url = "https://www.amazon.com/Copper-Pitcher-Lid-Handcrafted-Hammered/dp/B08LQTQM1D/?_encoding=UTF8&pd_rd_w=eiYYk&content-id=amzn1.sym.e4bd6ac6-9035-4a04-92a6-fc4ad60e09ad&pf_rd_p=e4bd6ac6-9035-4a04-92a6-fc4ad60e09ad&pf_rd_r=ZAJ35MJB3BZAMPC48JM6&pd_rd_wg=ljXYq&pd_rd_r=8b128ba0-fc89-4acd-a2ac-2044af3f54ba&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

# Headers passed into the request
headers = {
    "User-Agent": os.environ["User-Agent"],
    "Accept-Language": os.environ["Accept-Language"]
}

# Using requests to request the HTML page of product at site above
response = requests.get(amazon_url, headers=headers)
# print(response)
# text output
amazon_page = response.text

# instantiating soup class
soup = BeautifulSoup(amazon_page, "lxml")
# isolates tag which contains the price
price_loc = soup.find(class_="a-offscreen")

# isolate price as a floating point
price = float(price_loc.getText().split("$")[1])

# isolates item title
item_loc = soup.find(id="productTitle")
# get text and remove the space
item_title = item_loc.getText().strip()

print(price)
print(item_title)

# If the price is lower than the buying price send an email
buying_price = 200
if price < buying_price:
    message = f"{item_title} is now {price} \n\n{amazon_url}"
    # use smtplib to send email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # sending email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!:\n\n{message}")
