''' get data from eia total-energy api endpoint '''
# pylint: disable=C0103,W0311

import os
import json
import time
import datetime
import requests

from dateutil import rrule
from utils import helpers, meta

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
months = list(rrule.rrule(rrule.MONTHLY, dtstart=start, until=end))
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
      r = requests.get(url, timeout=300)
    except IOError as exc:
      raise IOError('cannot get: ', month) from exc

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
    with open(json_file, encoding='utf8') as f:
      j = json.load(f)
    pollution[month] = j['response']['data'][0]['value']

  print()
  print('POLLUTION', pollution)
  print()
  helpers.write_json('./pollution.json', pollution)
