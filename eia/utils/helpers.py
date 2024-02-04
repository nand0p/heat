import json
import os


def get_api_key(key_path):
  with open(key_path, 'r') as file:
    api_key = file.read().strip()
  api_key = '?api_key=' + api_key
  return api_key


def get_routes(j):
  r = []
  k = j.get('response')
  if k:
    kr = k.get('routes')
    print('routes', kr)
    if kr:
      for xr in kr:
        print('route', xr['id'])
        r.append(xr['id'])
  return r


def write_json(json_file, j):
  print('writing json file: ', json_file)
  try:
    with open(json_file, 'w') as out:
      json.dump(j, out)
  except:
    print('file_exists: ', json_file)



#dd.routes .response.routes[].id

 #"coal"
 #"crude-oil-imports"
 #"electricity"
 #"international"
 #"natural-gas"
 #"nuclear-outages"
 #"petroleum"
 #"seds"
 #"steo"
 #"densified-biomass"
 #"total-energy"
 #"aeo"
 #"ieo"
 #"co2-emissions"



def  ensure_data_dir(data_dir):
  if not os.path.exists(data_dir):
    print('making data dir: ', data_dir)
    try:
      os.mkdir(data_dir)
    except:
      pass
  else:
    print('data dir exists')
