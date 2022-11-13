# We use DataManager,FlightSearch, FlightData, NotificationManager classes
# to search Tequila API and organize the information as to update us when a
# cheap flight becomes available

# importing class from data_manager module
from data_manager import DataManager
from flight_search import FlightSearch
from _datetime import datetime, timedelta
from notification_manager import NotificationManager

# instantiating objects from class
data_manager = DataManager()
flight_object = FlightSearch()
notification_manager = NotificationManager()

# object method obtains data which can be stored in sheet_data,
# a list of dictionaries representing each row
sheet_data = data_manager.get_sheet_data()
# print(sheet_data)

#checking to see if iataCode column first row is empty in google sheets
if sheet_data[0]['iataCode'] == "":
    # iterating through each list items of sheet_data(google sheets rows)
    for row in sheet_data:
        # Using method from FlightSearch class, which needs city as input
        # we find IATA code and update it for given city/row, in sheet_data
        row['iataCode'] = flight_object.Get_IATA_Codes(row["city"])
    #sheet data variable is updated with sheet data with IATA codes
    #print(sheet_data)

    # We update city_data_prices from data manager after getting iata codes
    data_manager.city_data_prices = sheet_data
    # We can then update google sheets with iata codes using method
    data_manager.IATA_codes_sheet_update()

today = datetime.now()
# tomorrow's date and in 6 months
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)
# formatted dates because datetime returns (year,month,day)
# and api needs opposite
leave_tomorrow = tomorrow.strftime("%d/%m/%Y")
leave_six_months = six_months.strftime("%d/%m/%Y")

# for each destination city in sheet_data
# use find flight method from flight search class
# to find a flight in accordance with parameters entered
for city in sheet_data:
    trip = flight_object.Find_Flight(
        departure_city="LON",
        arrival_city=city["iataCode"],
        leave_tomorrow=leave_tomorrow,
        leave_six_months=leave_six_months
    )
    # if no flights are available let forloop continue to run when trip is None
    # because the method find_flight didn't return anything
    if trip is None:
        continue

    # if the price found by the Find_Flight method is
    # less than lowest price in google sheet
    if trip.price < city['lowestPrice']:
        sms = f"Cheap flight update. Only £{trip.price} to fly from{trip.cityFrom}-{trip.airport_from}"\
              f"to {trip.cityTo}-{trip.airport_to},from {trip.departure_date} to {trip.return_date}."
        # If there's a stopover add this to the text message
        if trip.stop_overs > 0:
            sms += f"\nFlight has {trip.stop_overs} stop over, via {trip.via_city}."
            print(sms)
        # send sms using text method
        notification_manager.text(sms)
