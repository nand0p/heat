from argparse import ArgumentParser

import matplotlib.pylab as plt
import requests
import pprint
import json
import sys


debug = False
d_raw = []
results = []
outfile = 'out.json'
logfile = 'log.json'
all_file = 'all_models.png'
hot_file = 'hot_models.png'
api_file = 'cmip56_forcing_feedback_ecs.json'
api_base = 'https://raw.githubusercontent.com/'
api_path = 'mzelinka/cmip56_forcing_feedback_ecs/master/'
api = api_base + api_path + api_file

parser = ArgumentParser()
parser.add_argument("-a", "--all-models", action="store_true", default=False)
parser.add_argument("-t", "--threshold", type=float, default=4.75)
parser.add_argument("-s", "--save", action="store_true", default=False)
args = parser.parse_args()

r = requests.get(api)
j = json.loads(r.text)

d_raw.append({'all_models': args.all_models})
d_raw.append({'api': api})
d_raw.append({'threshold': args.threshold})
d_raw.append({'debug': debug})
d_raw.append({'all_file': all_file})
d_raw.append({'hot_file': hot_file})
d_raw.append({'status': r.status_code})

for key1, val1 in j.items():
  for key2, val2 in val1.items():
    if isinstance(val2, dict):
      for key3, val3 in val2.items():
        if isinstance(val3, dict):
          results.append({key2: val3})

x_name = []
for model in results:
  for name, data in model.items():
    for model_type, model_data in data.items():
      if model_type == 'ECS':
        if model_data > args.threshold:
          plt.bar(name[0:2], model_data)
          x_name.append(name)
        elif model_data > args.threshold - 1:
          plt.bar(name[0:2], model_data)
        elif args.all_models == True:
          plt.bar(name[0:2], model_data)

plt.legend(set(x_name))
plt.ylabel('ECS DATA')
plt.title('EQUILIBRIUM CLIMATE SENSITIVITY')
if args.all_models:
  plt.xlabel('ALL MODELS')
  print('save', all_file)
  if args.save:
    plt.savefig(all_file)
else:
  plt.xlabel('HOT MODELS')
  print('save', hot_file)
  if args.save:
    plt.savefig(hot_file)

if not args.save:
  plt.show()

j = json.dumps(str(d_raw))
r = json.dumps(str(results))
print('saving ' + outfile)
with open(outfile, 'w', encoding='utf-8') as f:
  json.dump(r, f, ensure_ascii=False, indent=4)
print('saving ' + logfile)
with open(logfile, 'w', encoding='utf-8') as f:
  json.dump(j, f, ensure_ascii=False, indent=4)
