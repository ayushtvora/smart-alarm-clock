from fastapi import FastAPI
from dotenv import load_dotenv
import os
import pymongo
from WeatherClient import WeatherClient

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")
mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
weather_client = WeatherClient("vancouver")
app = FastAPI()


@app.get("/")
def root():
    return {"status": 200, "data": {"message": "Hello World"}}


@app.get("/weather-raw/")
def weather_raw():
    response = weather_client.get_weather_data_raw()
    return {"status": 200, "data": response}


@app.get("/weather-raw/{city}")
def weather_raw(city: str):
    weather_client.set_city(city)
    response = weather_client.get_weather_data_raw()
    return {"status": 200, "data": response}


@app.get("/weather/")
def weather():
    forecast = weather_client.get_weather_data()
    return {"status": 200, "data" : forecast}


@app.get("/weather/{city}")
def weather(city: str):
    weather_client.set_city(city)
    forecast = weather_client.get_weather_data()
    return {"status": 200, "data": forecast}


# @app.get("/user-info/{id}")
# async def user_info(id: int):
#
#     return {};