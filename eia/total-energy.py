from utils import helpers, meta
import requests
import json
import time
import os


api = 'https://api.eia.gov/v2/total-energy'
data_dir = 'data/total-energy'
api_key_path = '../eia.key'
api_pause = 0.01
month = '2023-10'
freq = 'monthly'
facet = 'TETCEUS'



api_key = helpers.get_api_key(api_key_path)
print('api_key', api_key)


helpers.ensure_data_dir(data_dir)
rx1 = requests.get(api + api_key)
meta.print_metadata(rx1)
j1 = rx1.json()
rx1.close() 	
helpers.write_json(data_dir + '/top-level.json', j1)

rx2_args = '&frequency=' + freq + \
           '&data[]=value' + \
           '&start=' + month + \
           '&end=' + month + \
           '&facets[msn][]=' + facet

rx2 = requests.get(api + '/data' + api_key + rx2_args)
meta.print_metadata(rx2)
j2 = rx2.json()
rx2.close()
helpers.write_json(data_dir + '/data-' + month + '.json', j2)
