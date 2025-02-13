import requests
import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = "" # Enter Amadeus API key
        self._api_secret = "" # Enter Amadeus API secret
        self._token = ""

    def _get_new_token(self):
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=token_url, headers=header, data=body)
        print(response.json())
        self._token = response.json()["access_token"]

    def _get_iata_code(self, city_name):
        cities_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {
            "authorization": f"Bearer {self._token}"
        }
        body = {
            "keyword": city_name
        }
        response = requests.get(url=cities_url, headers=header, params=body)
        # print(response.text)
        result = response.json() # ["data"][0]["iataCode"]
        # print(result)
        return result

    def _get_flight_offers(self, destination):
        offers_url = "https://test.api.amadeus.com/v1/shopping/flight-dates"
        header = {
            "Authorization": f"Bearer {self._token}"
        }
        today = datetime.datetime.today()
        dates = f'{(today+datetime.timedelta(days=1)).strftime("%Y-%m-%d")},{(today+datetime.timedelta(days=45)).strftime("%Y-%m-%d")}'
        params = {
            "origin": "LON",
            "destination": destination,
            "departureDate": dates,
            "nonStop": True
        }
        response = requests.get(url=offers_url, headers=header, params=params)
        # print(response.text)
        return response
