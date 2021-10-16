# Monitoring Device
| ID | Requirement | Test Cases |
|:---:|:---:|:---:|
| R1 | The monitoring device shall consume power. | TC1 |
| R2 | The monitoring device shall have a constant source of power | TC2 |
| R3 | The monitoring device shall read in ambient temperature. | TC3 |
| R4 | The monitoring device shall read in ambient humidity. | TC4 |
| R5 | The monitoring device shall read in ambient pressure. | TC5 |
| R6 | The monitoring device shall read in gas resistance. | TC6 |
| R7 | The monitoring device shall interact with the test harness via serial communication. | TC7 |
| R8 | The monitoring device shall display when the temperature is between 0° and 65° Celsius. | TC8 |
| R9 | The monitoring device shall display when the temperature exceeds 65° Celsius. | TC9 |
| R10 | The monitoring device shall display when the temperature exceeds 85° Celsius. | TC10 |
| R11 | The monitoring device shall display when the temperature below 0° Celsius. | TC11 |
| R12 | The monitoring device shall display when the temperature below -40° Celsius. | TC12 |
| R13 | The monitoring device shall display when the humidity is between 10% and 90% relative humidity. | TC13 |
| R14 | The monitoring device shall display when the humidity exceeds 90% relative humidity. | TC14 |
| R15 | The monitoring device shall display when the humidity exceeds 95% relative humidity. | TC15 |
| R16 | The monitoring device shall display when the humidity below 10% relative humidity. | TC16 |
| R17 | The monitoring device shall display when the pressure is between 8.85899 and 32.48298 inches of mercury.| TC17 |
| R18 | The monitoring device shall display when the pressure is below 8.85899 inches of mercury.| TC18 |
| R19 | The monitoring device shall display when the pressure exceeds 32.48298 inches of mercury. | TC19 |
| R20 | The monitoring device shall take sensor readings every \[time unit\]. | TC20 |

# Test Harness
| ID | Requirement | Test Cases |
|:---:|:---:|:---:|
| R21 | The test harness shall not interfere with the amount of power the monitoring device is consuming.| TC21 |
| R22 | The test harness shall log sensor data from the monitoring device into a CSV file.  | TC22 |
| R23 | The test harness shall log power consumption data of the monitoring device into a CSV file.  | TC23 |
| R24 | The test harness shall generate visualization of the sensor data from the monitoring device. | TC24 |
| R25 | The test harness shall generate visualization of the power consumption data of the monitoring device.  | TC25 |
| R26 | The test harness shall receive data from the monitoring device via serial communication. | TC26 |
| R27 | The test harness shall take power consumption readings every \[time unit\]. | TC27 |

# Meta
| ID | Requirement | Test Cases |
|:---:|:---:|:---:|
| R28 | The monitoring device cycles shall execute within 500 milliseconds. | TC28 |
| R29 | The test cases for the monitoring device shall execute within 500 milliseconds. | TC29 |

# Test Cases
| ID | Description | Steps | Input | Expected Output | Actual Output | Pass/Fail | Requirement Link |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| TC1 | INA219 power reading is nonzero | Run poweronly.py script, monitor printed output | N/A | Power value greater than 0 watts | Range of values > 0W | Pass | R1 |
| TC2 | Voltage constant within 7V and 12V for 30 seconds | Run poweronly.py script, monitor printed output for 30 seconds | N/A | Consistent voltage of 9.128V | Pass | R2 |
| TC3 | BME680 temperature attribute is not null | Print temperature value | Serial.print(bme680.temperature) | Non-null value | Non-null value | Pass | R3 |
| TC4 | BME680 humidity attribute is not null | Print humidity attribute | Serial.print(bme680.humidity) | Non-null value | Non-null value | Pass | R4 |
| TC5 | BME680 pressure attribute is not null | Print pressure attribute | Serial.print(bme680.pressure) | Non-null value | | Non-null value | Pass | R5 |
| TC6 | BME680 gas resistance attribute is not null | Print gas resistance attribute | Serial.print(bme680.gas_resistance) | Non-null value | Non-null value | Pass | R6 |
| TC7 | Serial communication is alive | Run logging program and verify serial input | N/A | Statement from Arduino printed to Pi terminal | Statements from Arduino are printed to Pi terminal | Pass | R7 |
| TC8 | Temperature value is between 0° and 65° Celsius | Set temperature value to 35° C | temperature = 35 | "Temperature is within the full accuracy range for the humidity and pressure sensors" printed to serial | "Temperature is within the full accuracy range for the humidity and pressure sensors" | Pass | R8 |
| TC9 | Temperature is greater than 65° Celsius | Set temperature value to 75° C | temperature = 75 | "Temperature has exceeded 65° C. Temperature is outside the full accuracy range for the humidity and pressure sensors" printed to serial | "Temperature has exceeded 65° C. Temperature is outside the full accuracy range for the humidity and pressure sensors" | Pass | R9 |
| TC10 | Temperature is greater than 85° Celsius | Set temperature to 95° C | temperature = 95 | "Temperature has exceeded 85° C. Temperature is outside the operational range for the BME680 sensor" printed to serial | "Temperature has exceeded 85° C. Temperature is outside the operational range for the BME680 sensor" | Pass | R10 |
| TC11 | Temperature is less than 0° Celsius | Set temperature to -10° C | temperature = -10 | "Temperature is below 0° C. Temperature is outside the full accuracy range for the humidity and pressure sensors" printed to serial | "Temperature is below 0° C. Temperature is outside the full accuracy range for the humidity and pressure sensors" | Pass | R11 |
| TC12 | Temperature is less than -40° Celsius | Set temperature to -50° C | temperature = -50 | "Temperature is below -40° C. Temperature is outside the operational range for the BME680 sensor" printed to serial | "Temperature is below -40° C. Temperature is outside the operational range for the BME680 sensor" | Pass | R12 |
| TC13 | Humidity is between 10% and 90% relative humidity | Set humidity to 50% rh | humidity = 50 | "Humidity is within the full accuracy range for the humidity sensor" printed to serial | "Humidity is within the full accuracy range for the humidity sensor" | Pass | R13 |
| TC14 | Humidity is greater than 90% relative humidity | Set humidity to 92.5% rh | humidity = 92.5 | "Humidity has exceeded 90% rh. Humidity is outside the full accuracy range for the humidity sensor" printed to serial | "Humidity has exceeded 90% rh. Humidity is outside the full accuracy range for the humidity sensor" | Pass | R14 |
| TC15 | Humidity is greater than 95% relative humidity | Set humidity to 97.5% rh | humidity = 97.5 | "Humidity has exceeded 95% rh. Humidity is outside the operational range for the gas sensor" printed to serial | "Humidity has exceeded 95% rh. Humidity is outside the operational range for the gas sensor" | Pass | R15 |
| TC16 | Humidity is less than 10% relative humidity | Set humidity to 5% rh | humidity = 5 | "Humidity is below 10% rh. Humidity is outside the operational range for the gas sensor" printed to serial | "Humidity is below 10% rh. Humidity is outside the operational range for the gas sensor" | Pass | R16 |
| TC17 | Pressure is between 8.85899 and 32.48298 inches of mercury | Set pressure to 20 inHg | pressure = 20 | "Pressure is within the full accuracy range for the pressure sensor" printed to serial | "Pressure is within the full accuracy range for the pressure sensor" | Pass | R17 |
| TC18 | Pressure is less than 8.85899 inches of mercury | Set pressure to 5 inHg | pressure = 5 | "Pressure is below the full accuracy range for the pressure sensor" | "Pressure is below the full accuracy range for the pressure sensor" | Pass | R18 |
| TC19 | Pressure is greater than 32.48298 inches of mercury | Set pressure to 35 inHg | pressure = 35 | "Pressure exceeds the full accuracy range for the pressure sensor" | "Pressure exceeds the full accuracy range for the pressure sensor" | Pass | R19 |
| TC20 | Sensor readings are taken every 5 seconds | Run bme680_v3, monitor serial output | N/A | Reading statement printed every 5 seconds | Reading statement printed every 5 seconds | Pass | R20 |
| TC21 | Test harness cannot interfere with power consumption of the monitoring device | Run poweronly.py with USB connection between monitoring device and test harness, then without USB connection, monitor outputs and compare | N/A | Power consumption does not change whether USB connection exists or not | Offset of ~10mA, ~0.2W, consistent | Fail | R21 |
| TC22 | Test harness logs sensor data into CSV file | Run arduinopower.log, upon completion check for presence of sensor-data CSV file | N/A | Timestamped sensor-data CSV file | CSV file exists | Pass | R22 |
| TC23 | Test harness logs power consumption data into CSV file | Run arduinopowerlog.py, upon completion check for presence of power-data CSV file | N/A | Timestamped power-data CSV file | CSV file exists | Pass | R23 |
| TC24 | Test harness generates graphs of the sensor data | Run sensorgraphs.py, visually confirm graph | N/A | Graph | Graph | Pass | R24 |
| TC25 | Test harness generates graphs of the power consumption data | Run powergraphs.py, visually confirm graph | N/A | Graph | Graph | Pass | R25 |
| TC26 | Test harness receives data from monitoring device via serial | Run arduinopowerlog.py, monitor printed output | N/A | On-screen output | On-screen output | Pass | R26 |
| TC27 | Power consumption readings are taken every 5 seconds | Run arduinopowerlog.py, compare timestamp | N/A | Reading every 5 seconds within 200 milliseconds | Reading frequency of 5 seconds with < 200ms variance | Pass | R27 |
| TC28 | Monitoring device cycles will execute within 500 milliseconds | Run bme680_v3, monitor timestamps | N/A | 500 milliseconds | < 500ms | Pass | R28 |
| TC29 | Non-visual test cases for monitoring device will execute within 500 milliseconds| Run several test cases, monitor timestamps | N/A | 500 milliseconds | < 500ms | Pass | R29 |

