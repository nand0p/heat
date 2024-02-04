from utils import helpers, meta
import requests
import json
import time
import os


api = 'https://api.eia.gov/v2/'
data_dir = 'routes/'
api_key_path = '../../eia.key'
api_pause = 0.001


api_key = helpers.get_api_key(api_key_path)
print('api_key', api_key)


print('executing top level')
helpers.ensure_data_dir(data_dir)
rx = requests.get(api + api_key)
meta.print_metadata(rx)
j = rx.json()
rx.close() 	

if j:
  helpers.write_json(data_dir + '/toplevel.json', j)
  routes = helpers.get_routes(j)
  if routes:
    helpers.write_json(data_dir + '/routes.json', routes)


print('processing routes')
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
for route in routes:
  print('--> executing route: ', api + route + api_key)
  print(count0, count1, count2, count3, count4, count5, count6)
  rr = requests.get(api + route + api_key)
  meta.print_metadata(rr)
  j = rr.json()
  rr.close()
  if j:
    helpers.write_json(data_dir + route + '.json', j)
    r1 = helpers.get_routes(j)
    if r1:
      helpers.ensure_data_dir(data_dir + route)
      helpers.write_json(data_dir + route + '/routes.json', r1)

  count0 = count0 + 1
  count6 = count6 + 1
  time.sleep(api_pause)

  for rx1 in r1:
    route1 = route + '/' + rx1
    print('----> executing route: ', api + route1 + api_key)
    print(count0, count1, count2, count3, count4, count5, count6)
    rr1 = requests.get(api + route1 + api_key)
    meta.print_metadata(rr1)
    j = rr1.json()
    rr1.close()
    if j:
      helpers.write_json(data_dir + route1 + '.json', j)
      r2 = helpers.get_routes(j)
      if r2:
        helpers.ensure_data_dir(data_dir + route1)
        helpers.write_json(data_dir + route1 + '/routes.json', r2)

    count1 = count1 + 1
    count6 = count6 + 1
    time.sleep(api_pause/2)

    for rx2 in r2:
      route2 = route + '/' + rx1 + '/' + rx2
      print('------> executing route: ', api + route2 + api_key)
      print(count0, count1, count2, count3, count4, count5, count6)
      rr2 = requests.get(api + route2 + api_key)
      meta.print_metadata(rr2)
      j = rr2.json()
      rr2.close()
      if j:
        helpers.write_json(data_dir + route2 + '.json', j)
        r3 = helpers.get_routes(j)
        if r3:
          helpers.ensure_data_dir(data_dir + route2)
          helpers.write_json(data_dir + route2 + '/routes.json', r3)

      count2 = count2 + 1
      count6 = count6 + 1
      time.sleep(api_pause/3)

      for rx3 in r3:
        route3 = route + '/' + rx1 + '/' + rx2 + '/' + rx3
        print('--------> executing route: ', api + route3 + api_key)
        print(count0, count1, count2, count3, count4, count5, count6)
        rr3 = requests.get(api + route3 + api_key)
        meta.print_metadata(rr3)
        j = rr3.json()
        rr3.close()
        if j:
          helpers.write_json(data_dir + route3 + '.json', j)
          r4 = helpers.get_routes(j)
          if r4:
            helpers.ensure_data_dir(data_dir + route3)
            helpers.write_json(data_dir + route3 + '/routes.json', r4)

        time.sleep(api_pause/4)
        count3 = count3 + 1
        count6 = count6 + 1

        for rx4 in r4:
          route4 = route + '/' + rx1 + '/' + rx2 + '/' + rx3 + '/' + rx4
          print('----------> executing route: ', api + route4 + api_key)
          print(count0, count1, count2, count3, count4, count5, count6)
          rr4 = requests.get(api + route4 + api_key)
          meta.print_metadata(rr4)
          j = rr4.json()
          rr4.close()
          if j:
            helpers.write_json(data_dir + route4 + '.json', j)
            r5 = helpers.get_routes(j)
            if r5:
              helpers.ensure_data_dir(data_dir + route4)
              helpers.write_json(data_dir + route4 + '/routes.json', r5)

          time.sleep(api_pause/5)
          count4 = count4 + 1
          count6 = count6 + 1

          for rx5 in r5:
            route5 = route + '/' + rx1 + '/' + rx2 + '/' + rx3 + '/' + rx4 + '/' + rx5
            print('============> executing route: ', api + route5 + api_key)
            print(count0, count1, count2, count3, count4, count5, count6)
            rr5 = requests.get(api + route5 + api_key)
            meta.print_metadata(rr5)
            j = rr5.json()
            rr5.close()
            if j:
              helpers.write_json(data_dir + route5 + '.json', j)
              r6 = helpers.get_routes(j)
              if r6:
                helpers.ensure_data_dir(data_dir + route5)
                helpers.write_json(data_dir + route5 + '/routes.json', r6)

            time.sleep(api_pause/6)
            count5 = count5 + 1
            count6 = count6 + 1
