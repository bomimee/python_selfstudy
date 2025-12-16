import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()



class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._SHEETY_USER_ENDPOINT = os.environ["SHEETY_USER_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(self._SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
    
    def update_destination_price(self, city_id, flight_data):
        new_data = {
            "price": {
            "lowestPrice": flight_data.price,
            "airline": flight_data.airline,
            "originAirport": flight_data.origin_airport,
            "destinationAirport": flight_data.destination_airport,
            "outDate": flight_data.out_date,
            "returnDate": flight_data.return_date
            }
        }
        response = requests.put(
            url=f"{self._SHEETY_PRICES_ENDPOINT}/{city_id}",
            json=new_data,
            auth=self._authorization
        )
        print(response.text)
    
    def get_customer_emails(self):
        response = requests.get(self._SHEETY_USER_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data
