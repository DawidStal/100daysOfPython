import flight_search
import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.amadeus = flight_search.FlightSearch()
        self.amadeus._get_new_token()

    def getPrices(self, data):
        answer = []
        for item in data["prices"]:
            print("Getting price for", item["city"])
            try:
                iataCode = self.amadeus._get_iata_code(item["city"])["data"][0]["iataCode"]
                # print(iataCode)
                try:
                    # Get flight offers
                    response = self.amadeus._get_flight_offers(iataCode)
                    minprice = 10000.0
                    origin = ""
                    departureDate = ""
                    returnDate = ""
                    try:
                        for ticket in response.json()["data"]:
                            # print(ticket["price"]["total"])
                            price = float(ticket["price"]["total"])  # float(ticket["price"]["total"])
                            if price < minprice:
                                origin = ticket["origin"]
                                departureDate = ticket["departureDate"]
                                returnDate = ticket["returnDate"]
                                minprice = price
                        print(minprice)
                        answer.append({"city": item["city"],
                                       "origin": origin,
                                       "destination": iataCode,
                                       "price": minprice,
                                       "sheetPrice": item["lowestPrice"],
                                       "departureDate": departureDate,
                                       "returnDate": returnDate})
                    except KeyError:
                        print("Error: Couldn't getting price")
                except NameError:
                    print(NameError, "error getting flight offers")
            except KeyError:
                print("Error: Couldn't get iata code")

        return answer
