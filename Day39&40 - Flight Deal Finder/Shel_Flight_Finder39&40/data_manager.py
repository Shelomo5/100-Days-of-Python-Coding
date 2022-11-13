import requests
import os

sheety_url = os.environ["sheety_url"]
sheety_url2 = os.environ["sheety_url2"]
#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        # creating dictionary to store data from google sheets
        self.city_data_prices = {}

    # method uses sheety api to get data from google sheet
    def get_sheet_data(self):
        sheet_response = requests.get(url=sheety_url2)
        # data is a dictionary with row information from google sheet
        data = sheet_response.json()
        # print(data["prices"])
        # data["prices"] is a list of each row from google sheet
        # self.city_data_prices is now a list of dictionaries
        self.city_data_prices = data["prices"]
        # method returns list of dictionaries with data from google sheets
        return self.city_data_prices

    # update google sheet with updated IATA codes using sheety API request
    def IATA_codes_sheet_update(self):
        # iterating through each item which represents a row of data stored in dictionary
        for item in self.city_data_prices:
            # JSON request updating iata code column in google sheets
            updated_data = {
                "price": {
                    'iataCode': item['iataCode']
                }
            }
            # added item number and 'id' at the end of url to specify row id per sheety documentation
            sheet_response = requests.put(url=f"{sheety_url2}/{item['id']}", json=updated_data)
            # print(sheet_response.text)


# data["prices"] =
# [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
# {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
# {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
# {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
# {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
# {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
# {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
# {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
# {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]