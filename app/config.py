import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("8ad8b16934816ccd7c783627e929a582")
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"