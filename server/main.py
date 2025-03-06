import bson
from fastapi import FastAPI

from WeatherClient import WeatherClient
from AtlasClient import AtlasClient


weather_client = WeatherClient("vancouver")
atlas_client = AtlasClient("alarm-clock-db")
current_user = None
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

@app.get("/mongo-view-dump/")
def mongo_ping():
    atlas_client.ping()
    collection = atlas_client.find("users")
    for doc in collection:
        del doc["_id"]
    return {"status": 200, "data": collection}

@app.get("/mongo-view-dump/{collection_name}")



@app.get("/user-info/{id}")
async def user_info(id: int):
    return {"status": 501}