from dateutil.rrule import rrule, MONTHLY
from utils import helpers, meta
import requests
import datetime
import json
import time
import os


pollution = {}
api = 'https://api.eia.gov/v2/total-energy/'
data_dir = 'total-energy'
api_key_path = '../../eia.key'
api_pause = 0.5
debug = False
freq = 'monthly'
facet = 'TETCEUS'
start = datetime.date(1975, 1, 1)
end = datetime.date(2023, 10, 1)
months = [m for m in rrule(MONTHLY, dtstart=start, until=end)]
api_key = helpers.get_api_key(api_key_path)
helpers.ensure_data_dir(data_dir)


for month in months:
  month = f"{month:%Y-%m}"
  print('===>POLLUTION', pollution, '<===')
  print('===>executing: ', month, '<===')

  url_args = '&frequency=' + freq + \
             '&data[]=value' + \
             '&start=' + month + \
             '&end=' + month + \
             '&facets[msn][]=' + facet

  url = api + 'data' + api_key + url_args
  json_file = data_dir + '/data-' + month + '.json'
  print('------>url', url)
  print('------>json_file', json_file)

  if not os.path.exists(json_file):
    try:
      r = requests.get(url)
    except:
      print('cannot get: ', month)

    if r:
      meta.print_metadata(r)
      j = r.json()
      r.close()

    if j:
      if debug:
        print('******* JSON', j, '********')

      pollution[month] = j['response']['data'][0]['value']
      helpers.write_json(json_file, j)

    if api_pause:
      time.sleep(api_pause)
  else:
    print('FILE EXISTS NOT HITTING API ', url)
    f = open(json_file)
    j = json.load(f)
    pollution[month] = j['response']['data'][0]['value']
    f.close()

print()
print('POLLUTION', pollution)
print()
helpers.write_json(data_dir + '/pollution.json', pollution)
