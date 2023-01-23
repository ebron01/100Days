import os
from twilio.rest import Client
class NotificationManager():
    def __init__(self):
    #This class is responsible for sending notifications with the 
    # deal flight details.
        # self.raw_data = data.sheety_response
        # self.cheapest_ticket_list = data.cheapest_ticket_list
        # self.notify_api_url = os.environ["NOTIFY_API_URL"]
        self.account_sid = os.environ["NOTIFY_API_SID"]
        self.auth_token = os.environ["NOTIFY_API_TOKEN"]
        # self.from_ = os.environ["NOTIFY_API_FROM"]
        # self.to = os.environ["NOTIFY_API_TO"]
        
    def notify(self, cheapest_ticket):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
                                    body=f'Low price alert!Only {cheapest_ticket["price"]}$ to fly from {cheapest_ticket["cityFrom"]}-{cheapest_ticket["flyFrom"]} to {cheapest_ticket["cityTo"]}-{cheapest_ticket["flyTo"]}, from {cheapest_ticket["local_arrival"].split("T")[0]} to {cheapest_ticket["local_departure"].split("T")[0]}.',
                                    from_= '+1 218 332 3260',
                                    to= '+93 731 599 599'
                                )
        print(message.status)
        