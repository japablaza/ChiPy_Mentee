#!/usr/bin/env python

import requests
import json

# url_4square = 'https://api.foursquare.com/v2/venues/explore'
url_4square = 'https://api.foursquare.com/v2/venues/search'

parametros = dict(
    client_id='S0YI4LO5DWBHNTYIEGIL1HDG2P4R5HDFD0RRAOY4YMJ3WZPD',
    client_secret='Z3JL003BUCCFGUW31P0XAV1SKM3QOP1HIW2YOYSLA4JCCA4O',
    # v='20180323',
    v='20180323',
    # ll='40.7243,-74.0018',
    ll=' 41.85, -87.65',
    # query='coffee',
    # limit=1
)

get_request = requests.get(url=url_4square, params=parametros)
resultado_get = json.loads(get_request.text)
fs_http_code = get_request.status_code

print(type(get_request))
print(type(resultado_get))
print(resultado_get)
print(fs_http_code)
