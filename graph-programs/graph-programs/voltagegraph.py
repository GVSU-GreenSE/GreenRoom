import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog as fd

x_ticks = []
voltage = []

filename = fd.askopenfilename()

#Reads data from csv into x and y value arrays
with open(filename,'r') as csvfile:
  lines = csv.reader(csvfile, delimiter=",")
  for row in lines:
    x_ticks.append(int(row[0]))
    voltage.append(float(row[2]))
      
#Reads first line and grabs timestamp        
with open(filename,'r') as f:
  reader = csv.reader(f, delimiter=",")
  row = next(reader)
  timestamp = row[5]
  
#format timestamp
timestamp = timestamp[:10] + " " + timestamp[11:13] + ":" + timestamp[14:]

#Creates figure and ax objects    
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)

ax1.grid(b=True, which='major', color='#666666', linestyle='-')
ax1.minorticks_on()  
ax1.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2) 

#Graph
ax1.plot(x_ticks,voltage, color='yellow')
ax1.set_xlabel("Ticks")
ax1.set_ylabel("Voltage (volts)")

ax1.set_xticks(np.arange(x_ticks[0], x_ticks[len(x_ticks) - 1] + 10, 10))    #Sets number of x-ticks
ax1.set_yticks(np.arange(5, 13, 1))  #Sets number of y-ticks
ax1.margins(x=0)

#Overall details
plt.suptitle("Voltage")
plt.figtext(x=0.42, y=0.93, s=timestamp)
plt.subplots_adjust(hspace=0.5)

plt.show()