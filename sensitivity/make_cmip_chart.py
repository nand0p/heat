import matplotlib.pylab as plt
import requests
import pprint
import json
import sys


all_models = False
debug = False
d_raw = []
api = 'https://raw.githubusercontent.com/mzelinka/cmip56_forcing_feedback_ecs/master/cmip56_forcing_feedback_ecs.json'
results = []
threshold = 4.75
outfile = 'out.json'
all_file = 'all_models.png'
hot_file = 'hot_models.png'

d_raw.append({'args': sys.argv})
d_raw.append({'api': api})
d_raw.append({'threshold': threshold})
d_raw.append({'debug': debug})
d_raw.append({'all_file': all_file})
d_raw.append({'hot_file': hot_file})

r = requests.get(api)
j = json.loads(r.text)

d_raw.append({'status': r.status_code})

for key1, val1 in j.items():
  for key2, val2 in val1.items():
    if isinstance(val2, dict):
      for key3, val3 in val2.items():
        if isinstance(val3, dict):
          results.append({key2: val3})

d_raw.append({'results': results})
x_name = []
for model in results:
  for name, data in model.items():
    for model_type, model_data in data.items():
      if model_type == 'ECS':
        if model_data > threshold:
          plt.bar(name[0:2], model_data)
          x_name.append(name)
        elif model_data > threshold - 1:
          plt.bar(name[0:2], model_data)
        #elif all_models == True:
        #  plt.bar(name[0:2], model_data)

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

j = json.dumps(str(d_raw))
print('saving ' + outfile)
with open(outfile, 'w', encoding='utf-8') as f:
  json.dump(j, f, ensure_ascii=False, indent=4)


