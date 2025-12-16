import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

URL = 'https://test.api.amadeus.com/v1/'
FLIGHT_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["API_KEY"]
        self._api_secret = os.environ["API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):

        header ={
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body= {
            "grant_type" : "client_credentials",
            "client_id":self._api_key,
            "client_secret":self._api_secret
        }
        response = requests.post(url=f"{URL}security/oauth2/token", headers=header, data=body)
        response.raise_for_status()
        token = response.json().get("access_token")
        return token

    def get_destination_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        parameters ={
            "keyword":city_name,
            "max":"2",
            "include":"AIRPORTS"
        }

        response = requests.get(f"{URL}reference-data/locations/cities", params=parameters, headers=headers)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
        
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop":  "true" if is_direct else "false",
            "currencyCode": "KRW",
            "max":"10"
        }

        response = requests.get(FLIGHT_ENDPOINT, params=query, headers=headers)
        if response.status_code != 200:
            print(f"check_flight() response_code: {response.status_code}")
            print("Response body:", response.text)
            return None
        
        return response.json()

        
