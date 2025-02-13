import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint
#
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
dmanager = DataManager()
data = dmanager.get_flight_data()
print(data)
data = dmanager.get_users_data()
print(data)
# fdata = FlightData()
# prices = fdata.getPrices(data)
# dmanager.send_notification(prices)
