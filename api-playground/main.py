from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")
app = FastAPI()


@app.get("/")
async def root():
    return {"status": 200, "data": {"message": "Hello World"}}


@app.get("/weather-raw/{city}")
async def weather_raw(city: str):
    response = await weather_api_call(city)
    return {"status": 200, "data": response}


@app.get("/weather/{city}")
async def weather(city: str):
    response = await weather_api_call(city)
    forecast = await parse_weather_data(response)
    return {"status": 200, "data" : forecast}


async def weather_api_call(city):
    url = "http://api.weatherapi.com/v1/forecast.json?"
    url += f"key={weather_api_key}&q={city}"
    response = requests.get(url).json()
    return response


async def parse_weather_data(response):
    response_day = response["forecast"]["forecastday"][0]

    hourly = [
        {
            "time": hour["time"],
            "time_epoch": hour["time_epoch"],
            "temp_c": hour["temp_c"],
            "condition": hour["condition"]["text"],
            "condition_icon": hour["condition"]["icon"],
        }
        for hour in response_day["hour"]
    ]

    forecast = {
        "date": response_day["date"],
        "date_epoch": response_day["date_epoch"],
        "min_temp_c": response_day["day"]["mintemp_c"],
        "max_temp_c": response_day["day"]["maxtemp_c"],
        "avg_temp_c": response_day["day"]["avgtemp_c"],
        "max_wind_kph": response_day["day"]["maxwind_kph"],
        "total_precip_mm": response_day["day"]["totalprecip_mm"],
        "will_rain": bool(response_day["day"]["daily_will_it_rain"]),
        "chance_of_rain": response_day["day"]["daily_chance_of_rain"],
        "will_snow": bool(response_day["day"]["daily_will_it_snow"]),
        "chance_of_snow": response_day["day"]["daily_chance_of_snow"],
        "uv_index": response_day["day"]["uv"],
        "sunrise": response_day["astro"]["sunrise"],
        "sunset": response_day["astro"]["sunset"],
        "condition": response_day["day"]["condition"]["text"],
        "condition_icon": response_day["day"]["condition"]["icon"],
        "hourly": hourly
    }

    return forecast