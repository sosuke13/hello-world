import requests
import json
from pprint import pprint

API_KEY = "589f3b79f24f66d279d1a4491c7b5547"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja"
city = "2130037"

response = requests.get(BASE_URL + "&id={}&APPID={}".format(city, API_KEY))
weather_data = json.loads(response.text)

pprint(weather_data['name']+"の天気は"+weather_data['weather'][0]['description']+"です。")

