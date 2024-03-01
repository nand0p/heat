import matplotlib.pylab as plt
import requests
import pprint
import json
import sys


debug = False
api = 'https://raw.githubusercontent.com/mzelinka/cmip56_forcing_feedback_ecs/master/cmip56_forcing_feedback_ecs.json'
results = []
threshold = 4.75
all_file = 'all_models.png'
hot_file = 'hot_models.png'

if debug:
  print('args: ', sys.argv)
  print('api: ', api)
  print('threshold: ', threshold)
  print('debug: ', debug)
  print('all_file: ', all_file)
  print('hot_file: ', hot_file)

if len(sys.argv) > 1:
  all_models = True
  print('...run all models...')
else:
  all_models = False
  print('...run hot models...')

r = requests.get(api)
j = json.loads(r.text)

if debug:
  print('status', r.status_code)
  print('text', r.text)
  print('content', r.content)

for key1, val1 in j.items():
  if debug:
    print('key1: ', key1)
    print('val1: ', val1)
  for key2, val2 in val1.items():
    if debug:
      print('key2: ', key2)
      print('val2: ', val2)

    if isinstance(val2, dict):
      for key3, val3 in val2.items():
        if isinstance(val3, dict):
          if debug:
            print('========================')
            print('key2: ', key2)
            print('key3: ', key3)
            print('data: ', val3)
            print('------------------------')
          results.append({key2: val3})

if debug:
  pprint.pprint(results)


x_name = []
for model in results:
  if debug:
    print('model', model)
  for name, data in model.items():
    if debug:
      print('name', name)
      print('data', data)
    for key, value in data.items():
      if debug:
        print('key: ', key)
        print('value: ', value)
      if key == 'ECS':
        if value > threshold:
          if debug:
            print('name: ', name)
          plt.bar(name[0:2], value)
          x_name.append(name)
        elif value > threshold - 1:
          plt.bar(name[0:2], value)
        elif all_models == True:
          plt.bar(name[0:2], value)

plt.legend(set(x_name))
plt.ylabel('ECS DATA')
plt.title('EQUILIBRIUM CLIMATE SENSITIVITY')
if all_models:
  plt.xlabel('ALL MODELS')
  print('save', all_file)
  plt.savefig(all_file)
else:
  plt.xlabel('HOT MODELS')
  print('save', hot_file)
  plt.savefig(hot_file)
