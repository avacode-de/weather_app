from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import CityRequest
from .crud import get_weather
from .models import WeatherResponse

app = FastAPI()

origins = {
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3000/weather"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.post("/weather", response_model=WeatherResponse)
def read_weather(request: CityRequest):
    try:
        weather = get_weather(request.city)
        return weather
    except Exception as e:
        raise HTTPException(status_code=404, detail="City not found")
