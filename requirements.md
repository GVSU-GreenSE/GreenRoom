# Monitoring Device
| ID | Requirement | Test Cases |
|:---:|:---:|:---:|
| R1 | The monitoring device shall consume power. | TC1 |
| R2 | The monitoring device shall have a steady source of power | TC2 |
| R3 | The monitoring device shall read in ambient temperature. | TC3 |
| R4 | The monitoring device shall read in ambient humidity. | TC4 |
| R5 | The monitoring device shall read in ambient pressure. | TC5 |
| R6 | The monitoring device shall read in gas resistance. | TC6 |
| R7 | The monitoring device shall interact with the test harness via serial communication. | TC7 |
| R8 | The monitoring device shall display when the temperature is above 0° Celsius and less than 65° Celsius. | TC8 |
| R9 | The monitoring device shall display when the temperature is at or exceeds 65° Celsius. | TC9 |
| R10 | The monitoring device shall display when the temperature is at or exceeds 85° Celsius. | TC10 |
| R11 | The monitoring device shall display when the temperature is at or below 0° Celsius. | TC11 |
| R12 | The monitoring device shall display when the temperature is at or below -40° Celsius. | TC12 |
| R13 | The monitoring device shall display when the humidity is at or exceeds 90% relative humidity. | TC13 |
| R14 | The monitoring device shall display when the humidity is at or exceeds 95% relative humidity. | TC14 |
| R15 | The monitoring device shall display when the humidity is at or below 10% relative humidity. | TC15 |
| R16 | The monitoring device shall display when the pressure is at or below 8.85899 inches of mercury.| TC16 |
| R17 | The monitoring device shall display when the pressure is at or exceeds 32.48298 inches of mercury. | TC17 |
| R18 | The monitoring device shall take sensor readings every \[time unit\]. | TC18 |

# Test Harness
| ID | Requirement | Test Cases |
|:---:|:---:|:---:|
| R19 | The test harness shall not interfere with the amount of power the monitoring device is consuming.| TC19 |
| R20 | The test harness shall log sensor data from the monitoring device into a CSV file.  | TC20 |
| R21 | The test harness shall log power consumption data of the monitoring device into a CSV file.  | TC21 |
| R22 | The test harness shall generate visualization of the sensor data from the monitoring device. | TC22 |
| R23 | The test harness shall generate visualization of the power consumption data of the monitoring device.  | TC23 |
| R24 | The test harness shall receive data from the monitoring device via serial communication. | TC24 |
| R25 | The test harness shall take power consumption readings every \[time unit\]. | TC25 |

# Meta
| ID | Requirement | Test Cases |
|:---:|:---:|:---:|
| R26 | The monitoring device cycles shall execute within \[time frame\] milliseconds. | TC26 |
| R27 | The test cases for the monitoring device shall execute within \[time frame\] milliseconds. | TC27 |
| R28 | The test cases for the test harness shall execute within \[time frame\] milliseconds. | TC29 |

# Monitoring Device Test Cases

# Test Harness Test Cases
