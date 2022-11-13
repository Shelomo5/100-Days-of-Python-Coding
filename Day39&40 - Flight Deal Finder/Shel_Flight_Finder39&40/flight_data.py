# class structures flight data and returns it in a single variable
# called trip, this class is instantiated in FlightSearch class
class FlightData:
    def __init__(self,cityFrom,cityTo,airport_from,airport_to,price,
                 departure_date,return_date,stop_overs=0,via_city=""):

        self.cityFrom = cityFrom
        self.cityTo = cityTo
        self.airport_from = airport_from
        self.airport_to = airport_to
        self.price = price
        self.departure_date = departure_date
        self.return_date = return_date

        self.stop_overs = stop_overs
        self.via_city = via_city
