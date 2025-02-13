import requests
from notification_manager import NotificationManager


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_id = "" # Enter sheety id
        self.sheety_flights_url = f"https://api.sheety.co/{self.sheety_id}/flightDeals/prices"
        self.sheety_users_url = f"https://api.sheety.co/{self.sheety_id}/flightDeals/users"
        self.notificationManager = NotificationManager()

    def get_flight_data(self):
        return requests.get(self.sheety_flights_url).json()

    def get_users_data(self):
        return requests.get(self.sheety_users_url).json()

    def send_notification(self, prices):
        print(prices)
        for item in prices:
            if item["price"] < item["sheetPrice"]:
                print(f"lower price for {item["city"]}")
                self.notificationManager.sendSMS(item)

    def send_email_notifications(self, prices):
        users = requests.get(self.sheety_users_url).json()["users"]
        user_emails = []
        for user in users:
            user_emails.append(user["email"])

        for item in prices:
            if item["price"] < item["sheetPrice"]:
                print(f"lower price for {item["city"]}")
                self.notificationManager.sendEmail(user_emails, item)

