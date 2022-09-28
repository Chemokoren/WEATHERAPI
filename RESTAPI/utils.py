import requests
from django.conf import settings


WEATHER_API_KEY = getattr(settings, "WEATHER_API_KEY", None)
if WEATHER_API_KEY is None:
    raise NotImplementedError("WEATHER_API_KEY must be set in the settings")

class WeatherAPI(object):
    def __init__(self):
        super(WeatherAPI, self).__init__()
        self.key = WEATHER_API_KEY



    def fetch_weather_data(self,city,days):
        self.api_url = 'http://api.weatherapi.com/v1/forecast.json?key={dc}&q={ct}&days={dy}&aqi=no&alerts=no'.format(
            dc=self.key,
            ct=city,
            dy=days
        )
        return requests.get(self.api_url, auth=("",self.key)).json()
