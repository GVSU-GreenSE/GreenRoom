import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog as fd

x_ticks  = []
bme680_temp = []
pressure = []
humidity = []
gas_resist  = []
tmp36_temp = []

x_tick_labels = ['0','10','20','30','40','50','60']

filename = fd.askopenfilename()

#Reads data from csv into x and y value arrays
with open(filename,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
      if row[1] == 'BME680':
        x_ticks.append(int(row[0]))
        bme680_temp.append(float(row[2]))
        pressure.append(float(row[3]))
        humidity.append(float(row[4]))
        gas_resist.append(float(row[5]))
      elif row[1] == 'TMP36':
        tmp36_temp.append(float(row[2]))
        
#Creates figure and ax objects    
fig,ax = plt.subplots(nrows=2,ncols=2,figsize=(10,6))
for row in ax: 
    for axis in row: 
        axis.grid(b=True, which='major', color='#666666', linestyle='-')
        axis.minorticks_on()  
        axis.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2) 

#Temperature graph
ax[0,0].plot(x_ticks, bme680_temp,color='#8B0000',label='BME680')
ax[0,0].plot(x_ticks, tmp36_temp,color='#FFA500',label='TMP36')

ax[0,0].set_title("Temperature")
ax[0,0].set_xlabel("Ticks")
ax[0,0].set_ylabel("Temp. (Degrees Celsius)")
ax[0,0].legend()

ax[0,0].set_xticks(np.arange(0, 70, 10))    #Sets number of x-ticks
ax[0,0].set_yticks(np.arange(22.00,33.0,1.0))  #Sets number of y-ticks
ax[0,0].margins(x=0)

#Pressure graph
ax[0,1].plot(x_ticks, pressure,color='#006400')

ax[0,1].set_title("Pressure")
ax[0,1].set_xlabel("Ticks")
ax[0,1].set_ylabel("Pressure (inches of mercury)")

ax[0,1].set_xticks(np.arange(0, 70, 10))    #Sets number of x-ticks
ax[0,1].set_yticks(np.arange(25.00, 33.00, 1.0))  #Sets number of y-ticks
ax[0,1].margins(x=0)

#Humidity graph
ax[1,0].plot(x_ticks, humidity,color='#0000FF')

ax[1,0].set_title("Humidity")
ax[1,0].set_xlabel("Ticks")
ax[1,0].set_ylabel("Humidity (%)")

ax[1,0].set_xticks(np.arange(0, 70, 10))    #Sets number of x-ticks
ax[1,0].set_yticks(np.arange(30, 65, 5))    #Sets number of y-ticks
ax[1,0].margins(x=0)

#Gas resistance graph
ax[1,1].plot(x_ticks, gas_resist,color='#9932CC')

ax[1,1].set_title("Gas Resistance")
ax[1,1].set_xlabel("Ticks")
ax[1,1].set_ylabel("Resistance (kOhms)")

ax[1,1].set_xticks(np.arange(0, 70, 10))    #Sets number of x-ticks
ax[1,1].set_yticks(np.arange(0, 90, 10))    #Sets number of y-ticks
ax[1,1].margins(x=0)

#Overall details
plt.suptitle("BME680 Sensor Data")
plt.subplots_adjust(hspace=0.5)

plt.show()
