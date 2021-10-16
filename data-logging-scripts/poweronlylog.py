#Takes power only readings for Arduino, while not logging Arduino serial data
import csv
import time
from ina219 import INA219

counter = 0
numreadings = 60
sleeptime = 5  #seconds between readings

#create INA219 object
ina = INA219(shunt_ohms=0.1,
             max_expected_amps = 0.01,
             address=0x40)
#configure ina
ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)
              
#timestamp for file names
timestamp = time.strftime("%Y-%m-%d_%H-%M", time.localtime())

#Prompt user for input about the experiment specifics
with open('poweronlylog.txt', "a") as f:
  f.write(timestamp)
  f.write(", No tests")
  f.write(", Power source: USB only\n")


while counter <= numreadings:
  #take power readings
  v = ina.voltage()
  i = ina.current()
  p = ina.power()
        
  #Formatted versions of voltage, current, power variables
  fv = '{0:0.1f}'.format(v)
  fi = '{0:0.2f}'.format(i)
  fp = '{0:0.4f}'.format(p/1000)
  #put data into a list to be processed for CSV
  power_data = [counter, 'INA219', fv, fi, fp]
  if counter == 0:
    power_data.append(timestamp)
  print (power_data)
        
  #open CSV for power consumption data and write to it
  with open(timestamp+'_power_only.csv','a') as f:  
    writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_NONE, escapechar = "\n")
    writer.writerow(power_data)
          
  counter += 1
  time.sleep(sleeptime)

