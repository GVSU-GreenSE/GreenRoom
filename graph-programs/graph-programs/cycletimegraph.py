import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter import filedialog as fd

x_ticks = []
looptime = []
looptesttime = []
testtime = []

filename = fd.askopenfilename()

#Reads data from csv into x and y value arrays
with open(filename,'r') as csvfile:
  lines = csv.reader(csvfile, delimiter=",")
  for row in lines:
    if row[1] == 'LoopTime':
      x_ticks.append(int(row[0]))
      looptime.append(int(row[2]))
    elif row[1] == 'LoopTestTime':
      looptesttime.append(int(row[2]))
    elif row[1] == 'TestTime':
      testtime.append(int(row[2]))
      
#Reads first line and grabs timestamp        
with open(filename,'r') as f:
  reader = csv.reader(f, delimiter=",")
  row = next(reader)
  timestamp = row[6]
  
#format timestamp
timestamp = timestamp[:10] + " " + timestamp[11:13] + ":" + timestamp[14:]

#Creates figure and ax objects    
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)

ax1.grid(b=True, which='major', color='#666666', linestyle='-')
ax1.minorticks_on()  
ax1.grid(b=True, which='minor', color='#999999', linestyle='-',alpha=0.2) 

#Graph
ax1.plot(x_ticks,looptime, color='blue', label='Main Cycle')
if len(looptesttime) > 0:
  ax1.plot(x_ticks,looptesttime, color='red', label='Main Cycle Tests')
if len(testtime) > 0:
  ax1.plot(x_ticks,testtime, color='green', label='Downtime Tests')
  
ax1.set_xlabel("Ticks")
ax1.set_ylabel("Time (milliseconds)")

ax1.set_xticks(np.arange(x_ticks[0], x_ticks[len(x_ticks) - 1] + 10, 10))    #Sets number of x-ticks
ax1.set_yticks(np.arange(200, 900, 100))  #Sets number of y-ticks
ax1.margins(x=0)

#Overall details
plt.suptitle("Arduino Execution Times")
plt.figtext(x=0.42, y=0.93, s=timestamp)
plt.subplots_adjust(hspace=0.5)
plt.legend()
plt.show()