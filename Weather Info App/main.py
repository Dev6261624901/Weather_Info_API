from fastapi import FastAPI
from weather_api import get_weather

app = FastAPI(
    title="🌤️ Weather Info API",
    description="Get real-time weather data for any city using OpenWeatherMap API. Returns temperature, humidity, and weather description.",
    version="1.0.0"
)
@app.get("/")
def home():
    return {"message": "Welcome to Weather API"}

from fastapi import FastAPI, Query
from typing import Annotated

@app.get("/weather/", summary="Get Weather for a City", description="Returns temperature, humidity, and weather description for a given city.")
async def weather(
    city: Annotated[
        str,
        Query(
            title="City Name",
            description="Name of the city to fetch weather for (e.g. London, Delhi, New York)",
            example="Delhi"
        )
    ]
):
    result = await get_weather(city)
    return result
