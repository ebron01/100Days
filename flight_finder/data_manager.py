import os 
import requests
from flight_search import FlightSearch
from notification_manager import NotificationManager

class DataManager(FlightSearch, NotificationManager):
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        super().__init__()
        self.SHEETY_PRICES_URL = os.environ["SHEETY_PRICES_URL"]
        self.sheety_headers = {
        "Authorization" : os.environ["SHEETY_AUTHORIZATION"],
        "Content-Type":"application/json"
        }
        self.sheety_response = self.getalldata()
        self.cities = self.citylister()
        self.iota = self.queryloc(self.cities)
        self.querywriter()
    
    def querywriter(self):
        line_start = 2
        for iota in self.iota:
            params = {"price"  : {"iotaCode" : iota}}
            requests.put(url=f"{self.SHEETY_PRICES_URL}/{line_start}", json=params, headers=self.sheety_headers)
            line_start += 1

    def pricewriter(self):
        return None
    
    def getalldata(self):
        return requests.get(url=self.SHEETY_PRICES_URL, headers=self.sheety_headers).json()
    
    def citylister(self):
        return [key["city"] for key in self.sheety_response["prices"]]

    def check_price(self):
        for index in range(len(self.cheapest_ticket_list)):
            try:
            # if self.cheapest_ticket_list[index] == {}:
            #     continue
                cheapest = float(self.cheapest_ticket_list[index]['price']) 
                current = float(self.sheety_response['prices'][index]["lowestPrice"])
                if cheapest < current:
                    self.notify(self.cheapest_ticket_list[index])
            except:
                continue