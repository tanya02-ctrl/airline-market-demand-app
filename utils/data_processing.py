import os
import requests
from collections import defaultdict
from dotenv import load_dotenv

# Load API_KEY from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# AviationStack API URL
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_api_data():
    """
    Fetch flight data from the AviationStack API.
    Returns a list of flight dictionaries.
    """
    if not API_KEY:
        print("❌ API_KEY not found. Please set it in .env file.")
        return []

    params = {
        "access_key": API_KEY,
        "limit": 100  # Adjust if needed
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print(f"❌ Error fetching data from API: {e}")
        return []

def process_api_data(api_data):
    """
    Process API data to extract average price per route.
    Since AviationStack does not provide price, we simulate it.
    Returns a dictionary: {route: average_price}
    """
    route_prices = defaultdict(list)

    for flight in api_data:
        try:
            dep = flight["departure"]["airport"]
            arr = flight["arrival"]["airport"]
            if dep and arr:
                # Simulated price (replace with real pricing logic if available)
                mock_price = 100 + hash(dep + arr) % 200
                route = f"{dep} → {arr}"
                route_prices[route].append(mock_price)
        except Exception:
            continue

    # Calculate average price for each route
    avg_prices = {
        route: round(sum(prices) / len(prices), 2)
        for route, prices in route_prices.items() if prices
    }

    return avg_prices
