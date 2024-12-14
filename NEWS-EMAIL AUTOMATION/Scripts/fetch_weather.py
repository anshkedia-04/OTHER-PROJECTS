import requests

import sys
import os


# Add the root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.api_keys import WEATHER_API_KEY
from config.settings import WEATHER_URL

def fetch_weather(city="New York"):
    try:
        params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}
        response = requests.get(WEATHER_URL, params=params)
        weather_data = response.json()
        return (
            f"Weather in {city}:\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Condition: {weather_data['weather'][0]['description']}\n"
        )
    except Exception as e:
        return f"Error fetching weather: {e}"
