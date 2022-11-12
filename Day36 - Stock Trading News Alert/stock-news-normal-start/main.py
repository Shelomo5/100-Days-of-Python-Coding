import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = os.environ["stock_api_key"]
news_api_key = os.environ["news_api_key"]

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

# API parameters
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
    "language": "en",
    "sortBy": "popularity"
}

# API request
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
# put in json format
stock_data = response.json()
# get data for each day
stock_data_dict = stock_data["Time Series (Daily)"]
# use list comprehension to turn dict into a list of the values only for each day
# we're only interested in the values
data_list = [value for (key, value) in stock_data_dict.items()]
# isolate yesterday's closing stock price
yesterday_close = float(data_list[0]['4. close'])
print(yesterday_close)

# day before yesterday closing stock price
day_before_close = float(data_list[1]['4. close'])
print(day_before_close)

# difference between yesterday and today's price
difference = (yesterday_close - day_before_close)

rise_decrease = None
# if difference is positive print and up arrow and vice vers
if difference > 0:
    rise_decrease ="⬆️"
else:
    rise_decrease = "⬇️"

# Converting to percentage difference
percentage_difference = abs(round((difference / yesterday_close) * 100))

# If percentage is greater than 5 then get first 3 stories from newsapi.
if percentage_difference > .1:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_articles = response.json()['articles']
    three_articles = news_articles[:3]
    # print(news_articles)

# Creating a list of the first 3 articles headline and description using list comprehension.
article_list = [f"\n {STOCK_NAME}: {rise_decrease}{percentage_difference}% \n Headline: {article['title']}. \n\nDescription: {article['description']}" for article in three_articles]
# print(article_list)

# code from Twilio to send sms, create client object from client class
client = Client(account_sid, auth_token)

# use for loop to send 3 messages seperately which are formatted in list comprehension
for article in article_list:
    message = client.messages.create(
        body = article,
        from_='+19402835625',
        to= os.environ["to_phone"]
    )
    print(message.status)


