import geocoder
import requests
from .config import WEATHER_API_KEY, WEATHER_API_URL
from .models import WeatherResponse

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    else:
        return Exception("Unable to get a current location")
    
def get_weather_by_location(lat: float, lon: float) -> WeatherResponse:
    response = requests.get(
        WEATHER_API_URL,
        params= {
            "lat": lat,
            "lon": lon,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }
    )
    data = response.json()
    if response.status_code != 200:
        raise Exception(data.get("message", "Error fetching weather data"))
    


def get_weather(city: str = None) -> WeatherResponse:
    if city:
        response = requests.get(
            WEATHER_API_URL,
            params={
                "q": city,
                "appid": WEATHER_API_KEY,
                "units": "metric"
            }
        )
    else:
        lat, lon = get_current_location()
        response = requests.get(
            WEATHER_API_URL,
            params= {
                "lat": lat,
                "lon": lon,
                "appid": WEATHER_API_KEY,
                "units": "metric"
            }
        )
    data = response.json()
    if response.status_code != 200:
        raise Exception(data.get("message", "Error fetching weather data"))
    
    return WeatherResponse(
        temperature=data["main"]["temp"],
        description=data["weather"][0]["description"],
        city=data["name"]
    )
