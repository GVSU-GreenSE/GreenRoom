import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog as fd

x_ticks  = []
voltage = []
current = []
power = []

x_tick_labels = ['0','10','20','30','40','50','60']

filename = fd.askopenfilename()

#Reads data from csv into x and y value arrays
with open(filename,'r') as csvfile:
  lines = csv.reader(csvfile, delimiter=",")
  for row in lines:
    x_ticks.append(int(row[0]))
    current.append(float(row[3]))
    power.append(float(row[4]))
    
#Creates figure and ax objects    
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.grid(b=True, which='major', color='#666666', linestyle='-')
ax1.minorticks_on()  
ax1.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2) 
ax2.grid(b=True, which='major', color='#666666', linestyle='-')
ax2.minorticks_on()  
ax2.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2) 

#Current graph - in milliAmps
ax1.plot(x_ticks, current,color='#006400')

ax1.set_title("Current")
ax1.set_xlabel("Ticks")
ax1.set_ylabel("Current (milliAmps)")

ax1.set_xticks(np.arange(0, 65, 5))    #Sets number of x-ticks
ax1.set_yticks(np.arange(40.00, 56.00, 1.0))  #Sets number of y-ticks
ax1.margins(x=0)

#Power graph - in watts
ax2.plot(x_ticks, power,color='#9932CC')

ax2.set_title("Power")
ax2.set_xlabel("Ticks")
ax2.set_ylabel("Power (watts)")

ax2.set_xticks(np.arange(0, 65, 5))    #Sets number of x-ticks
ax2.set_yticks(np.arange(0.3500, 0.5500, 0.05))  #Sets number of y-ticks
ax2.margins(x=0)

#Overall details
plt.suptitle("INA219 Data")
plt.subplots_adjust(hspace=0.5)

plt.show()