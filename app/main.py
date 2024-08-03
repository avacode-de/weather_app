from fastapi import FastAPI, HTTPException
from .schemas import CityRequest
from .crud import get_weather
from .models import WeatherResponse

app = FastAPI()

@app.post("/weather", response_model=WeatherResponse)
def read_weather(request: CityRequest):
    try:
        weather = get_weather(request.city)
        return weather
    except Exception as e:
        raise HTTPException(status_code=404, detail="City not found")
