import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import math

df =pd.read_csv('/home/pi/Documents/data.csv', sep=',')
x= df.to_numpy()

new = []
count = 0
for i in range (0,math.ceil(len(x)/60)): #Creating an array of 24 list for each hour
    new.append([])

j=0
for k in range (len(x)): #For each hour, creating 60 array for the timestamps (0-59 mins)
    if count == 60:
        j += 1
        count = 0
    new[j].append(x[k])
    count += 1
    
#Sorting algorithm (Bubble sort)
for i in range (0,math.ceil(len(x)/60)-1): #0 - 23
    n = len(new[0])
    for j in range (n-1):
      for k in range (0,n-j-1): #0 - 59
          if new[i][k][0] > new[i][k+1][0]:
              new[i][k],new[i][k+1] = new[i][k+1],new[i][k]
              
for i in range (math.ceil(len(x)/60)-1,math.ceil(len(x)/60)): #24
    n = len(new[23])
    for j in range (n-1):
      for k in range (0,n-j-1): #0 - 59
          if new[i][k][0] > new[i][k+1][0]:
              new[i][k],new[i][k+1] = new[i][k+1],new[i][k]
              
with open('/home/pi/Documents/csv_pv','w') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp","total_load_kw","irradiance"])
    for i in range (math.ceil(len(x)/60)-1):
        for j in range (60):
            writer.writerow(new[i][j])
    for k in range (58):
        writer.writerow(new[23][k])
        
print(new)