#!/usr/bin/env python

import json
from prompt_toolkit import prompt
import requests

# The city_list.json file can be downloaded from link below
# http://bulk.openweathermap.org/sample/city.list.json.gz

with open('city_list.json', 'r') as cities_list:
    countries = json.load(cities_list)

country_code = ''
city = ''
while not country_code or not city:
    country_code = prompt('Pick a Country: ')
    city = prompt('If you know the city enter it here: ')
    # ToDo list after this part gets completed
    # 1. Names must match Dictionary values
    # 1.1. Research for ways to do this
    # 2. I think the next IF could be in the while loop to
    if not country_code or not city:
        print('You must type country and city')
        print('Try again\n')
    # 3. Add 'cls' to clean the screen
new_country = []

for k in range(0, len(countries)):
    if countries[k]['country'] == country_code:
        new_country.append(countries[k])

for l in range(0, len(new_country)):
    if new_country[l]['name'] == city:
        city_id = new_country[l]['id']

print(' ')
print('This is the ID for ' + city + ' city: ' + str(city_id))

# URL Example
# "https://api.openweathermap.org/data/2.5/weather?id=3873544&appid=7a2d438e1e09ea12a9d4c1a12ff46f58"

# print('API endpoint we generarate after selecting Country and City')
city_id = str(city_id)
domainid = 'https://api.openweathermap.org/data/2.5/weather?id='
appid = '7a2d438e1e09ea12a9d4c1a12ff46f58'
url = domainid + city_id + '&appid=' + appid
print(url)

get_url = requests.get(url)
http_code = get_url.status_code
resultado_get_url = json.loads(get_url.text)

print('HTTP code from ' + city + ' ID: ' + str(http_code))
print('Endo of the testing script')
print('='*60)
print(' ')

print(resultado_get_url)
print(http_code)
