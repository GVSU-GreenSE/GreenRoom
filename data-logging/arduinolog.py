#Logs sensor data from Arduino & BME680, logs power consumption data
import serial
import csv
import time
from ina219 import INA219

counter = 0
numreadings = 60

#create INA219 object
ina = INA219(shunt_ohms=0.1,
             max_expected_amps = 0.01,
             address=0x40)
#configure ina
ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)
              
#open serial port - default baudrate 9600
ser = serial.Serial('/dev/ttyUSB0') 
ser.flushInput()    #Clear the queue

#timestamp for file names
timestamp = time.strftime("%Y-%m-%d_%H-%M", time.localtime())

#Prompt user for input about the experiment specifics
with open('experimentlog.txt', "a") as f:
  f.write(timestamp)
  #print("Tests: ")
  #tests = input()
  #f.write(", Tests: " + tests + "\n")
  f.write(", Tests: All, main & downtime\n")

#Runs until keyboard interrupt
while counter <= numreadings:
  #Read from serial and decode
  ser_bytes = ser.readline()
  decoded_bytes = ser_bytes[0:len(ser_bytes) - 2].decode("utf-8")   
  
  #will only run if line starts with a digit - AKA is a reading  
  if decoded_bytes[0].isdigit():
    #splits read-in line to be processed for CSV
    split_bytes = decoded_bytes.split(' ')
    counter = int(split_bytes[0])
    if counter > numreadings:
      print ("All done!")
      break
    #only append timestamp to first line
    if counter == 0:
      split_bytes.append(timestamp)
    
    print (split_bytes)
    
    #open CSV for sensor data and write to it
    if split_bytes[1] == 'BME680' or split_bytes[1] == 'TMP36':   
      with open(timestamp+'_sensor_data.csv','a') as f:
        writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_NONE, escapechar = "\n")
        writer.writerow(split_bytes) 
    else:
      #open CSV for timing data and write to it
      with open(timestamp+'_timing_data.csv','a') as f:
        writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_NONE, escapechar = "\n")
        writer.writerow(split_bytes)   
        
    if split_bytes[1] == 'TMP36':  #this is done so the ina219 doesn't read twice per arduino tick
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
      with open(timestamp+'_power_data.csv','a') as f:  
        writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_NONE, escapechar = "\n")
        writer.writerow(power_data)
  else:
    #prints any non-reading messages
    print (decoded_bytes)


ser.close() 
