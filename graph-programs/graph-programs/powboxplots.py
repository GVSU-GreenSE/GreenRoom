import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wilcoxon, mannwhitneyu

datasum = 0
index = []

#Lists to store averages of replicates for each config
baseline_avgs = []
all_main_avgs = []
all_downtime_avgs = []
all_both_avgs = []

#For graph
boxdata = []
x_labels = ["Baseline", "All tests, main cycle", "All tests, downtime", "All tests, both cycles"]
yaxislabel = ""
title = ""

#Current or power
datapoint = input("Datapoint: ")

#Index for current or power varies
if datapoint == 'current':
  index = 3
  yaxislabel = "Current (milliamps)"
  title = "Current"
elif datapoint == 'power':
  index = 4
  yaxislabel = "Power (watts)"
  title = "Power"
 
#Calculate averages for baseline "No tests" config 
path = "/home/pi/Documents/pythoncode/power-data/no-tests"
os.chdir(path)

for file in os.listdir():
  with open(file,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
      datasum = datasum + float(row[index])
    baseline_avgs.append(float('{0:0.4f}'.format(datasum / 61)))
    datasum = 0
  
#Calculate averages for "All tests, main cycle" config
path = "/home/pi/Documents/pythoncode/power-data/all-tests-main-cycle"
os.chdir(path)
    
for file in os.listdir():
  with open(file,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
      datasum = datasum + float(row[index])
    all_main_avgs.append(float('{0:0.4f}'.format(datasum / 61)))
    datasum = 0
     
#Calculate averages for "All tests, downtime" config  
path = "/home/pi/Documents/pythoncode/power-data/all-tests-downtime"
os.chdir(path)    

for file in os.listdir():
  with open(file,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
      datasum = datasum + float(row[index])
    all_downtime_avgs.append(float('{0:0.4f}'.format(datasum / 61)))
    datasum = 0
    
#Calculate averages for "All tests, both cycles" config
path = "/home/pi/Documents/pythoncode/power-data/all-tests-both"
os.chdir(path)

for file in os.listdir():
  with open(file,'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for row in lines:
      datasum = datasum + float(row[index])
    all_both_avgs.append(float('{0:0.4f}'.format(datasum / 61)))
    datasum = 0
    
#Wilcoxon
print("Wilcoxon p-values")
stat, pvalue = wilcoxon(baseline_avgs, all_main_avgs)
print("Baseline v. All tests, main cycle: " + str(pvalue))
stat, pvalue = wilcoxon(baseline_avgs, all_downtime_avgs)
print("Baseline v. All tests, downtime: " + str(pvalue))
stat, pvalue = wilcoxon(baseline_avgs, all_both_avgs)
print("Baseline v. All tests, both cycles: " + str(pvalue))
    
#Mann-Whitney-U
print("Mann-Whitney-U p-values")
stat, pvalue = mannwhitneyu(baseline_avgs, all_main_avgs)
print("Baseline v. All tests, main cycle: " + str(pvalue))
stat, pvalue = mannwhitneyu(baseline_avgs, all_downtime_avgs)
print("Baseline v. All tests, downtime: " + str(pvalue))
stat, pvalue = mannwhitneyu(baseline_avgs, all_both_avgs)
print("Baseline v. All tests, both cycles: " + str(pvalue))   
    
#Graphing time

boxdata = [baseline_avgs, all_main_avgs, all_downtime_avgs, all_both_avgs]

fig = plt.figure(1,figsize=(8,6))
ax = fig.add_subplot(111)

bp = ax.boxplot(boxdata, patch_artist=True)

#Design
for box in bp['boxes']:
  box.set(color='#4B0082',linewidth=2)
  box.set(facecolor='#BA55D3')

for whisker in bp['whiskers']:
  whisker.set(color='#4B0082',linewidth=2)

for cap in bp['caps']:
  cap.set(color='#4B0082',linewidth=2)

for median in bp['medians']:
  median.set(color='#800000',linewidth=2)

for flier in bp['fliers']:
  flier.set(marker='D',color='48D1CC',alpha=0.5)

#Axis formatting
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

#Labels
ax.set_xticklabels(x_labels)
ax.set_ylabel(yaxislabel)
plt.suptitle("detroit box city")

plt.show()