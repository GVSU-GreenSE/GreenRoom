import os
import csv
from scipy.stats import wilcoxon, mannwhitneyu

datasum = 0
counter = 1
index = []

#Lists to store averages of replicates for each config
baseline_avgs = []
all_both_avgs = []

#Current or power
datapoint = input("Datapoint: ")

#Index for current or power varies
if datapoint == 'current':
  index = 3
  title = "Current"
elif datapoint == 'power':
  index = 4
  title = "Power"
elif datapoint == 'voltage':
  index = 2
  title = "Voltage"
 
#Calculate averages for baseline "No tests" config 
path = "/home/pi/Documents/greenroom/power-data/no-tests"
os.chdir(path)
print ("Baseline")

for file in os.listdir():
  if file.endswith("csv"): # ensure that the file is a CSV
    with open(file,'r') as csvfile:
      lines = csv.reader(csvfile, delimiter=",")
      for row in lines:
        datasum = datasum + float(row[index])
      baseline_avgs.append(datasum / 61.0)
      print ("Replicate " + str(counter) + ": " + str(datasum / 61.0))
      datasum = 0
      counter += 1
counter = 1  
 
#Calculate averages for "All tests, both cycles" config
path = "/home/pi/Documents/greenroom/power-data/all-tests-both"
os.chdir(path)
print ("All tests, main cycle & downtime") 

for file in os.listdir():
  if file.endswith("csv"): # ensure that the file is a CSV
    with open(file,'r') as csvfile:
      lines = csv.reader(csvfile, delimiter=",")
      for row in lines:
        datasum = datasum + float(row[index])
      all_both_avgs.append(datasum / 61.0)
      print ("Replicate " + str(counter) + ": " + str(datasum / 61.0))
      datasum = 0
      counter += 1
counter = 1  
    
#Wilcoxon
print("Wilcoxon p-values for " + title)
stat, pvalue = wilcoxon(baseline_avgs, all_both_avgs)
print("Baseline v. All tests, main cycle & downtime: " + str(pvalue))
       