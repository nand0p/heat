from utils import helpers, meta
import requests
import json
import time
import os


api = 'https://api.eia.gov/v2/'
data_dir = 'routes/'
api_key_path = '../../eia.key'
api_pause = None
#api_pause = 0.1


api_key = helpers.get_api_key(api_key_path)
print('api_key', api_key)
print('api_pause', api_pause)




#
# note: use recursion below
#

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0  # total routes described
count7 = 0  # total routes found

print('processing routes')
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
    count7 = count7 + 1
    helpers.write_json(data_dir + '/routes.json', routes)
    for route in routes:
      print('--> executing route: ', api + route + api_key)
      print(count0, count1, count2, count3, count4, count5, count6, ' - routes_found: ', count7)
      r0 = requests.get(api + route + api_key)
      meta.print_metadata(r0)
      j = r0.json()
      r0.close()
      if j:
        helpers.write_json(data_dir + route + '.json', j)
        rr0 = helpers.get_routes(j)
        if rr0:
          count7 = count7 + 1
          helpers.ensure_data_dir(data_dir + route)
          helpers.write_json(data_dir + route + '/routes.json', rr0)
    
      count0 = count0 + 1
      count6 = count6 + 1
      if api_pause:
        time.sleep(api_pause)
    
      for rx0 in rr0:
        route1 = route + '/' + rx0
        print('----> executing route: ', api + route1 + api_key)
        print(count0, count1, count2, count3, count4, count5, count6, ' - routes_found: ', count7)
        r1 = requests.get(api + route1 + api_key)
        meta.print_metadata(r1)
        j = r1.json()
        r1.close()
        if j:
          helpers.write_json(data_dir + route1 + '.json', j)
          rr1 = helpers.get_routes(j)
          if rr1:
            count7 = count7 + 1
            helpers.ensure_data_dir(data_dir + route1)
            helpers.write_json(data_dir + route1 + '/routes.json', rr1)
    
        count1 = count1 + 1
        count6 = count6 + 1
        if api_pause:
          time.sleep(api_pause/2)
    
        for rx1 in rr1:
          route2 = route + '/' + rx0 + '/' + rx1
          print('------> executing route: ', api + route2 + api_key)
          print(count0, count1, count2, count3, count4, count5, count6, ' - routes_found: ', count7)
          r2 = requests.get(api + route2 + api_key)
          meta.print_metadata(r2)
          j = r2.json()
          r2.close()
          if j:
            helpers.write_json(data_dir + route2 + '.json', j)
            rr2 = helpers.get_routes(j)
            if rr2:
              count7 = count7 + 1
              helpers.ensure_data_dir(data_dir + route2)
              helpers.write_json(data_dir + route2 + '/routes.json', rr2)
    
          count2 = count2 + 1
          count6 = count6 + 1
          if api_pause:
            time.sleep(api_pause/3)
    
          for rx2 in rr2:
            route3 = route + '/' + str(rx0) + '/' + rx1 + '/' + rx2
            print('--------> executing route: ', api + route3 + api_key)
            print(count0, count1, count2, count3, count4, count5, count6, ' - routes_found: ', count7)
            r3 = requests.get(api + route3 + api_key)
            meta.print_metadata(r3)
            j = r3.json()
            r3.close()
            if j:
              helpers.write_json(data_dir + route3 + '.json', j)
              rr3 = helpers.get_routes(j)
              if rr3:
                count7 = count7 + 1
                helpers.ensure_data_dir(data_dir + route3)
                helpers.write_json(data_dir + route3 + '/routes.json', rr3)
    
            count3 = count3 + 1
            count6 = count6 + 1
            if api_pause:
              time.sleep(api_pause/4)
    
            for rx3 in rr3:
              route4 = route + '/' + str(rx0) + '/' + rx1 + '/' + rx2 + '/' + rx3
              print('----------> executing route: ', api + route4 + api_key)
              print(count0, count1, count2, count3, count4, count5, count6, ' - routes_found: ', count7)
              r4 = requests.get(api + route4 + api_key)
              meta.print_metadata(r4)
              j = r4.json()
              r4.close()
              if j:
                helpers.write_json(data_dir + route4 + '.json', j)
                rr4 = helpers.get_routes(j)
                if rr4:
                  count7 = count7 + 1
                  helpers.ensure_data_dir(data_dir + route4)
                  helpers.write_json(data_dir + route4 + '/routes.json', rr4)
    
              count4 = count4 + 1
              count6 = count6 + 1
              if api_pause:
                time.sleep(api_pause/5)
    
              for rx4 in rr4:
                route5 = route + '/' + str(rx0) + '/' + rx1 + '/' + rx2 + '/' + rx3 + '/' + rx4
                print('============> executing route: ', api + route5 + api_key)
                print(count0, count1, count2, count3, count4, count5, count6, ' - routes_found: ', count7)
                r5 = requests.get(api + route5 + api_key)
                meta.print_metadata(r5)
                j = r5.json()
                r5.close()
                if j:
                  helpers.write_json(data_dir + route5 + '.json', j)
                  rr5 = helpers.get_routes(j)
                  if rr5:
                    count7 = count7 + 1
                    helpers.ensure_data_dir(data_dir + route5)
                    helpers.write_json(data_dir + route5 + '/routes.json', rr5)
    
                count5 = count5 + 1
                count6 = count6 + 1
                if api_pause:
                  time.sleep(api_pause/6)
