import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv('/home/pi/Documents/csv_pv', sep=',')

#df['total_load_kw'][df['total_load_kw'] < 0] = 0
list1 = []
for i in range (1,24):
    for j in range (60):
        list1.append(i)

for j in range (58):
    list1.append(24)
   
for i in range (len(list1)):
    df['timestamp'][i] = str(list1[i])+ ":" + df['timestamp'][i]
df['pv'] = df['irradiance']/700*63
df['difference'] = np.maximum((df['total_load_kw'] - df['pv']),0)
df['Genset'] = df['difference']*0.3

print(df['pv'])
x = df['timestamp']
y = df['total_load_kw']
z = df['difference']
a = df['Genset']
df['hour'] = list1

print(df['Genset'])


#z = df['PV']

plt.plot(x,z, color = 'g', linestyle = 'dashed',
        label = "Difference")
plt.plot(x,df['pv'], color = 'y', linestyle = 'dashed',
        label = "PV")
plt.plot(x,a, color = 'r', linestyle = 'dashed',
        label = "Genset")
  
plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('kW')
plt.title('Overview of Active Power', fontsize = 20)
plt.grid()
plt.legend()
plt.show()