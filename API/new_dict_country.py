#!/usr/bin/env python

import json
from prompt_toolkit import prompt

'''
This is an attempt of moving all cities from the US
to once dictionary called cities_us
'''

with open('city_list.json', 'r') as cities_list:
    countries = json.load(cities_list)

print(type(countries))  # This is a list made of dictionary
print(type(countries[1]))  # This a dictionary from once city

print(countries[1]['country'])


def city_country(country_code):
    cities_in = []
    for country in countries:
        if country['country'] == country_code:
            cities_in.append(country)
            country_code = cities_in[:]
            print(country_code)


pais = prompt('Select country. You can use US or CL: ')
city_country(pais)
