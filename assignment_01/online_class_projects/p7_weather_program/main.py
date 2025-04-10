import requests
from pprint import pprint

API_KEY = '98fbe15450e15b07ea5096b4788477b6'

city = input("Enter city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

weather_data = requests.get(base_url).json()
pprint(weather_data)


