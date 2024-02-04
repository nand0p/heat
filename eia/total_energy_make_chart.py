import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json



data_dir = './'
json_file = data_dir + 'pollution.json'
png_out = data_dir + 'pollution.png'


f = open(json_file)
j = json.load(f)
f.close()


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
plt.xlabel("1975 - Months - 2023")  # add X-axis label
plt.ylabel("Million Metric Tons")  # add Y-axis label
plt.title("CO2 Emissions United States") 
plt.savefig(png_out)
plt.show()
plt.close()
