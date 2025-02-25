from dotenv import load_dotenv
import os
import requests


class WeatherClient:
    def __init__(self, city: str):
        self.weather_data_raw = None
        self.weather_data = None
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "http://api.weatherapi.com/v1/forecast.json?"
        self.city = city
        self.update_weather_data()

    def get_weather_data(self):
        self.update_weather_data()
        return self.weather_data


    def get_weather_data_raw(self):
        self.update_weather_data()
        return self.weather_data_raw

    def set_city(self, city: str):
        self.city = city
        return self.city


    def update_weather_data(self):
        url = self.base_url + f"key={self.api_key}&q={self.city}"
        self.weather_data_raw = requests.get(url).json()
        self.weather_data = self.parse_raw()


    def parse_raw(self, response=None):
        if response is None:
            response = self.weather_data_raw

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
            "city": response["location"]["name"],
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