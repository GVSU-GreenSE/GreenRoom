import os
import csv
from scipy.stats import wilcoxon, mannwhitneyu

cursum = 0
powsum = 0
counter = 1

#Lists to store averages of replicates for each config
baseline_cur_avgs = []
all_both_cur_avgs = []
baseline_pow_avgs = []
all_both_pow_avgs = []

#Calculate averages for baseline "No tests" config 
path = "../ina219-data/no-tests"
os.chdir(path)
print ("Baseline")

for file in os.listdir():
  if file.endswith("csv"): # ensure that the file is a CSV
    with open(file,'r') as csvfile:
      lines = csv.reader(csvfile, delimiter=",")
      for row in lines:
        cursum = cursum + float(row[3]) #current
        powsum = powsum + float(row[4]) #power
      baseline_cur_avgs.append(cursum / 61.0)
      baseline_pow_avgs.append(powsum / 61.0)
      print ("Replicate " + str(counter) + ": Current, " + str(cursum / 61.0) + " Power, " + str(powsum / 61.0))
      cursum = 0
      powsum = 0
      counter += 1
counter = 1  
 
#Calculate averages for "All tests, both cycles" config
path = "../all-both"
os.chdir(path)
print ("All tests, main cycle & downtime") 

for file in os.listdir():
  if file.endswith("csv"): # ensure that the file is a CSV
    with open(file,'r') as csvfile:
      lines = csv.reader(csvfile, delimiter=",")
      for row in lines:
        cursum = cursum + float(row[3]) #current
        powsum = powsum + float(row[4]) #power
      all_both_cur_avgs.append(cursum / 61.0)
      all_both_pow_avgs.append(powsum / 61.0)
      print ("Replicate " + str(counter) + ": Current, " + str(cursum / 61.0) + " Power, " + str(powsum / 61.0))
      cursum = 0
      powsum = 0
      counter += 1
counter = 1  
    
#Wilcoxon
print("Wilcoxon p-values comparing baseline (no tests) and all tests, both cycles (p < 0.05)")
stat, pvalue = wilcoxon(baseline_cur_avgs, all_both_cur_avgs)
print("Current: " + str(pvalue))
stat, pvalue = wilcoxon(baseline_pow_avgs, all_both_pow_avgs)
print("Power: " + str(pvalue))
       