import requests
from datetime import timedelta


class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops, airline=None):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport= destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.airline = airline
        self.stops = stops
    
def find_cheapest_flight(data):
    """Amadeus API 결과에서 최저가 항공편을 찾아 반환 (편도/왕복 모두 지원)"""
    if data is None or "data" not in data or not data["data"]:
        print("⚠️ No flight data")
        return FlightData(price="N/A",
        origin_airport="N/A",
        destination_airport="N/A",
        out_date="N/A",
        return_date="N/A",
        stops="N/A",
        airline="N/A")

    flights = data["data"]
    cheapest_flight = None
    lowest_price = float("inf")

    for flight in flights:
        try:
            price = float(flight["price"]["grandTotal"])
        except (KeyError, ValueError):
            continue

        # 1. 출발 구간 정보
        outbound = flight["itineraries"][0]["segments"][0]
        origin = outbound["departure"]["iataCode"]
        destination = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
        out_date = outbound["departure"]["at"].split("T")[0]
        airline = outbound.get("carrierCode", "N/A")
        nr_stops = len(flight["itineraries"][0]["segments"]) - 1

        # 2️⃣ 귀국 정보 (있는 경우만)
        if len(flight["itineraries"]) > 1 and flight["itineraries"][1]["segments"]:
            return_seg = flight["itineraries"][1]["segments"][0]
            return_date = return_seg["departure"]["at"].split("T")[0]
        else:
            return_date = "N/A"

        # 3️⃣ 최저가 갱신
        if price < lowest_price:
            lowest_price = price
            cheapest_flight = FlightData(
                price=lowest_price,
                origin_airport=origin,
                destination_airport=destination,
                out_date=out_date,
                return_date=return_date,
                airline=airline,
                stops=nr_stops
            )

    if cheapest_flight:
        print(
            f"💰 Lowest price to {cheapest_flight.destination_airport} is ₩{cheapest_flight.price} "
            f"via {cheapest_flight.airline} ({cheapest_flight.out_date} → {cheapest_flight.return_date})"
        )
        return cheapest_flight
    else:
        print("⚠️ No valid flights found.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")