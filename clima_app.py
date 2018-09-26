#!/usr/bin/env python

import json
from prompt_toolkit import prompt
import requests

with open('city_list.json', 'r') as cities_list:
    countries = json.load(cities_list)

country_code = prompt('Give the country you would like to check the weather: ')
city = prompt('If you know the city enter it here: ')

new_country = []

for k in range(0, len(countries)):
    if countries[k]['country'] == country_code:
        new_country.append(countries[k])

for l in range(0, len(new_country)):
    if new_country[l]['name'] == city:
        city_id = new_country[l]['id']

print(city_id)

# URL Example
# "https://api.openweathermap.org/data/2.5/weather?id=3873544&appid=7a2d438e1e09ea12a9d4c1a12ff46f58"

city_id = str(city_id)
domainid = 'https://api.openweathermap.org/data/2.5/weather?id='
appid = '7a2d438e1e09ea12a9d4c1a12ff46f58'
url = domainid + city_id + '&appid=' + appid
print(url)
