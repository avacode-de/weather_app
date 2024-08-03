import requests
from .config import WEATHER_API_KEY, WEATHER_API_URL
from .models import WeatherResponse

def get_weather(city: str) -> WeatherResponse:
    response = requests.get(WEATHER_API_URL, params={"q": city, "appid": WEATHER_API_KEY, "units": "metric"})
    data = response.json()
    return WeatherResponse(
        temperature=data["main"]["temp"],
        description=data["weather"][0]["description"],
        city=data["name"]
    )