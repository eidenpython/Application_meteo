import requests
import datetime as dt
from tkinter import *

base_url = "https://api.openweathermap.org/data/2.5/weather?"

key = "c956f34308cf1ecb933aa5e907a01ac8"

city = "La Louvière"

lang = "fr"

url = base_url + "appid=" + key + "&q=" + city + "&lang=" + lang

def kelvin_to_celsuis_fahrenheit(kelvin):
    celsuis = kelvin - 273.15
    fahrenheit = celsuis * (9/5) + 32
    return celsuis, fahrenheit

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsuis_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsuis_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
weather1 = response['weather'][0]['main']
vue_distance = response['visibility']
nuage_pourcent = response['clouds']['all']
pression = response['main']['pressure']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])



