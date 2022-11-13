import requests
from flight_data import FlightData
from pprint import pprint
import os

Tequila_Endpoint = "https://tequila-api.kiwi.com/"
Tequila_API_KEY = os.environ["Tequila_API_KEY"]

#This class is responsible for talking to the Flight Search API.
class FlightSearch:
    # method gets IATA code from Tequila api
    def Get_IATA_Codes(self, city_name):
        locations_endpoint = f"{Tequila_Endpoint}locations/query"
        headers = {"apikey":Tequila_API_KEY}
        query = {"term": city_name, 'location_types': "city"}
        response = requests.get(url=locations_endpoint, headers=headers, params=query)
        code_data = response.json()
        # isolating code from API response
        IATA_code = code_data['locations'][0]['code']
        return IATA_code

    # method finds available flights from tequila api
    # according to certain parameters
    def Find_Flight(self, departure_city, arrival_city, leave_tomorrow, leave_six_months):
        Search_Endpoint = "http://tequila-api.kiwi.com/v2/search"

        query = {
            "fly_from": departure_city,
            "fly_to": arrival_city,
            "date_from":leave_tomorrow,
            "date_to":leave_six_months,
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        headers = {"apikey": Tequila_API_KEY}

        response = requests.get(url=Search_Endpoint, params=query, headers=headers)

        # Creating try and except in case no flights are found
        try:
            data = response.json()["data"][0]
            pprint(data)
        # if flights not found check if there are flights with one stopover
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=Search_Endpoint, params=query, headers=headers)
            # Creating try and except in case flight with one stopover are not found
            try:
                data = response.json()["data"][0]
                pprint(data)
            except IndexError:
                return None
            else:
                # Instantiating FlightData class
                flight_data = FlightData(
                    cityFrom = data["route"][0]["cityFrom"],
                    cityTo = data["route"][1]["cityTo"],
                    airport_from = data["route"][0]['flyFrom'],
                    airport_to = data["route"][1]['flyTo'],
                    price = data["price"],
                    departure_date = data["route"][0]["local_departure"].split("T")[0],
                    return_date = data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city= data["route"][0]["cityTo"]
                )
                # Print city and price for all cities
                print(f"{flight_data.cityTo}: £ {flight_data.price}")
                return flight_data

        else:
            flight_data = FlightData(
                cityFrom=data["route"][0]["cityFrom"],
                cityTo=data["route"][0]["cityTo"],
                airport_from=data["route"][0]['flyFrom'],
                airport_to=data["route"][0]['flyTo'],
                price=data["price"],
                departure_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            # Print city and price for all cities
            print(f"{flight_data.cityTo}: £ {flight_data.price}")
            return flight_data


