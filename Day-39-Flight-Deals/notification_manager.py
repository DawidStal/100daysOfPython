import os
from twilio.rest import Client

class NotificationManager:


    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)

    def sendSMS(self, data):

        message = self.client.messages.create(
            body=f"Low price alert! Only {data["price"]} to fly from {data["origin"]} to {data["destination"]} on {data["departureDate"]} until {data["returnDate"]}",
            from_="ENTER TWILIO NUMBER",
            to="ENTER YOUR NUMBER",
        )