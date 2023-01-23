import os 
import requests
from datetime import datetime, timedelta
from notification_manager import NotificationManager

FLY_FROM = "IST"
class FlightSearch(NotificationManager):
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        super().__init__()
        self.URL = os.environ["URL"]
        self.SEARCH_URL = self.URL + "v2/search"
        self.LOC_URL = self.URL + "locations/query"
        self.presentday = datetime.now()
        self.date_from = (self.presentday + timedelta(1)).strftime('%d/%m/%Y')
        self.date_to = (self.presentday + timedelta(180)).strftime('%d/%m/%Y')
        self.search_params = {
            "fly_from" : FLY_FROM,
            "fly_to" : "",
            "date_from" : self.date_from, 
            "date_to" : self.date_to, 
            }
        self.query_params = {
            "location_types" : "city",
            "term" : "",
            }
        self.headers = {
            "apikey" : os.environ["FLIGHT_SEARCH_API_KEY"],
        }
        self.cheapest_ticket_list = []
        # https://api.tequila.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
    
    def search(self, iota_list):
        for index in range(len(iota_list)):
            self.search_params["fly_to"] = iota_list[index]
            self.response = requests.get(url=self.SEARCH_URL, params=self.search_params, headers=self.headers).json()["data"]
            price = 30000 #an expensive ticket price to start of
            cheapest_ticket = {}
            for response in self.response:
                if response["price"] < price:
                    cheapest_ticket = response
                    price = response["price"]
            self.cheapest_ticket_list.append(cheapest_ticket)    
        return self.cheapest_ticket_list

    def queryloc(self, query_params):
        responses = []
        if len(query_params) > 1:
            for query in query_params:
                self.query_params["term"] = query
                response = requests.get(url=self.LOC_URL, params=self.query_params, headers=self.headers).json()
                responses.append(response["locations"][0]["code"])
        else:
            self.query_params["term"] = query_params
            responses = requests.get(url=self.LOC_URL, json=self.query_params)
        return responses

    