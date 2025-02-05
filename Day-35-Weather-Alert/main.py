import os
import requests
from twilio.rest import Client

account_sid = '' # Insert Twilio Account SID here
auth_token = os.environ.get("TWILIO_AUTH_TOKEN") # Get Auth Token for Twilio
print(auth_token)
APIkey = os.environ.get("OMW_API_KEY") # Get API Key for Open Weather Map
print(APIkey)
# Parameters
weather_params = {
    "lat": 0.0, # Insert latitude here
    "lon": 0.0, # Insert longitude here
    "appid": APIkey,
    "cnt": 4
}
# Get today's forecast for every 3 hours
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
rain = False
# Check each hour for rain
for item in response.json()["list"]:
    print(item["weather"])
    if item["weather"][0]["id"] < 600:
        rain = True
# If it's going to rain send an SMS
if rain:
    print("It's going to rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain",
        from_='', # insert twilio number here
        to='' # insert recieving number here
    )
