import httpx
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("Weather_API_KEY")

if not api_key:
    raise ValueError("Weather_API_KEY not found in environment variables!")
API_KEY = api_key

async def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if response.status_code == 200:
            return {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            return {"error": data["message"]}
