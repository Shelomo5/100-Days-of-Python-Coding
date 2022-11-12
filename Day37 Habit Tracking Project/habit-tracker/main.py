import requests
from datetime import datetime
import os

pixela_endpoint = os.environ["pixela_endpoint"]
USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPHID = os.environ["GRAPHID"]

# parameters needed for post request
users_param = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsOfService': "yes",
    "notMinor": 'yes',
}
# sending params in json format for request
# response = requests.post(url=pixela_endpoint, json=users_param)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph request made including headers
# response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(response.text)

# cycling graph html:https://pixe.la/v1/users/shelomo/graphs/graph1.html

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

# Time module for current date
today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?\n"),
}
# request to post pixel data point
response = requests.post(url=pixel_create_endpoint, json=pixel_param, headers=headers)

update_param = {
    "quantity": "1",
}

# endpoint url to update yesterday's pixel
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
# # updating yesterday's data point
# response = requests.put(url=update_endpoint, json=update_param, headers=headers)


# deleting yesterday's data point
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

# delete response
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)