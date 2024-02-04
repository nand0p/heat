''' eia data make line chart of total energy co2 emissions '''
# pylint: disable=C0103,W0311

import json
import numpy as np
import matplotlib.pyplot as plt



data_dir = './'
json_file = data_dir + 'pollution.json'
png_out = data_dir + 'pollution.png'

with open(json_file, encoding='utf8') as f:
  j = json.load(f)

print()
print('POLLUTION', j)
print()

co2 = []
months = []
for value in j.values():
  co2.append(float(value))
for month in j.keys():
  months.append(month)

np_co2 = np.array(co2)
time = np.array(months)

plt.plot(time, np_co2)
plt.xlabel("1975 - Months - 2023")
plt.ylabel("Million Metric Tons")
plt.title("CO2 Emissions United States")
plt.savefig(png_out)
plt.show()
plt.close()
