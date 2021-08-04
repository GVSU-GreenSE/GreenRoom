/* Takes temp, pressure, humidity, and gas resistance sampling
 *  Prints sensorID, tick, and sensor data to serial
 *  Temp in degrees Celsius
 *  Relative humidity in %
 *  Barometric pressure in inHg
 *  Gas resistance in KOhms
 *  Individual functions for all test cases (not needed for TC3 - TC6)
 *  Test cases called during every reading
 */
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"

#define MAIN_TESTS_ENABLED true
#define DOWNTIME_TESTS_ENABLED true

#define TEMP_TESTS_ENABLED true
#define HUMIDITY_TESTS_ENABLED true
#define PRESSURE_TESTS_ENABLED true

#define OPERATIONAL_TESTS_ENABLED false
#define RANGE_TESTS_ENABLED false

Adafruit_BME680 bme;
const int TMP36Pin = A0;

int tick = 0;
unsigned int lastReading = millis();
unsigned int readingDelay = 5000;
boolean testsRun = false;

void setup() {
  Serial.begin(9600);
  if(!bme.begin()){
    Serial.println(F("Could not find valid BME680 sensor - check wiring"));  
  }else{
    Serial.println(F("Reading begun"));  
  }

  //Oversampling & filter initilization - settings from bme680test example
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150); // 320*C for 150 ms
}

void loop() {
  unsigned int timeNow = millis();
  unsigned int loopStart = millis();
  
  if(timeNow - lastReading > readingDelay || tick == 0){
    //Sets internal member variables for BME (temperature, humidity, pressure, gas_resistance)
    if (! bme.performReading()) {
      Serial.println(F("Failed to perform reading :("));
      return;
    }
    
    //Prints tick
    Serial.print(tick);
    Serial.print(F(" "));

    //SensorID
    Serial.print(F("BME680 "));
  
    Serial.print(bme.temperature);  //TC3
    Serial.print(F(" "));

    //Pressure reading is in pascals - divide by 3386.39 to get inHg
    Serial.print(bme.pressure / 3386.39, 5);  //TC5
    Serial.print(F(" "));

    Serial.print(bme.humidity); //TC4
    Serial.print(F(" "));

    //Reading is in Ohms, divide by 1000 to get kiloOhms
    Serial.println(bme.gas_resistance / 1000.0, 2); //TC6

  
    //TMP36
    Serial.print(tick);
    Serial.print(F(" "));

    Serial.print(F("TMP36 "));

    int sensorVal = analogRead(TMP36Pin); //Get ADC reading
    float voltage = (sensorVal / 1024.0) * 5.0; //Convert ADC reading to voltage
    float temp = (voltage - 0.5) * 100; //Convert voltage to temp in Celsius
    Serial.println(temp);

    if(MAIN_TESTS_ENABLED){
      unsigned int loopTestsStart = millis();
      if(TEMP_TESTS_ENABLED){
        tempInRange(bme.temperature);
        tempAboveAccuracyRange(bme.temperature);
        tempAboveOperationalRange(bme.temperature);
        tempBelowAccuracyRange(bme.temperature);
        tempBelowOperationalRange(bme.temperature);   
      }
      if(HUMIDITY_TESTS_ENABLED){
        humidityInRange(bme.humidity);
        humidityAboveAccuracyRange(bme.humidity);
        humidityAboveOperationalRange(bme.humidity);  
      }
      if(PRESSURE_TESTS_ENABLED){
        pressureInRange(bme.pressure);
        pressureBelowAccuracyRange(bme.pressure);
        pressureAboveAccuracyRange(bme.pressure);  
      }
      if(OPERATIONAL_TESTS_ENABLED){
        tempAboveOperationalRange(bme.temperature);
        tempBelowOperationalRange(bme.temperature);
        humidityAboveOperationalRange(bme.humidity);
      }
      if(RANGE_TESTS_ENABLED){
        tempInRange(bme.temperature);
        humidityInRange(bme.humidity);
        pressureInRange(bme.pressure);  
      }
      unsigned int loopTestsEnd = millis();
      Serial.print(tick);
      Serial.print(F(" "));
      Serial.print("LoopTestTime ");
      Serial.println(loopTestsEnd - loopTestsStart);
    }

    testsRun = false;
    lastReading = timeNow;  //Reset timer
    
    unsigned int loopEnd = millis();
    Serial.print(tick);
    Serial.print(F(" "));
    Serial.print("LoopTime ");
    Serial.println(loopEnd - loopStart);
    tick++;
  }else if(!testsRun && DOWNTIME_TESTS_ENABLED){
    delay(2500);
    unsigned int testStart = millis();
    //Downtime testing
    if(TEMP_TESTS_ENABLED){
      tempInRange(bme.temperature);
      tempAboveAccuracyRange(bme.temperature);
      tempAboveOperationalRange(bme.temperature);
      tempBelowAccuracyRange(bme.temperature);
      tempBelowOperationalRange(bme.temperature);   
    }
    if(HUMIDITY_TESTS_ENABLED){
      humidityInRange(bme.humidity);
      humidityAboveAccuracyRange(bme.humidity);
      humidityAboveOperationalRange(bme.humidity);  
    }
    if(PRESSURE_TESTS_ENABLED){
      pressureInRange(bme.pressure);
      pressureBelowAccuracyRange(bme.pressure);
      pressureAboveAccuracyRange(bme.pressure);  
    }
    if(OPERATIONAL_TESTS_ENABLED){
      tempAboveOperationalRange(bme.temperature);
      tempBelowOperationalRange(bme.temperature);
      humidityAboveOperationalRange(bme.humidity);
    }
    if(RANGE_TESTS_ENABLED){
        tempInRange(bme.temperature);
        humidityInRange(bme.humidity);
        pressureInRange(bme.pressure);  
    }
    
    testsRun = true;

    unsigned int testEnd = millis();
    Serial.print(tick - 1);
    Serial.print(F(" "));
    Serial.print(F("TestTime "));
    Serial.println(testEnd - testStart);
  }
}

//TC8 - temp between 0° and 65° (inclusive)
void tempInRange(float temp){
  if(temp >= 0.0 && temp <= 65.0){
    Serial.println(F("Temperature is within the full accuracy range for the humidity and pressure sensors"));  
  } 
}

//TC9 - temp greater than 65° (exclusive)
void tempAboveAccuracyRange(float temp){
  if(temp > 65.0){
    Serial.println(F("Temperature has exceeded 65° C"));
    Serial.println(F("Temperature is outside the full accuracy range for the humidity and pressure sensors")); 
  } 
}

//TC10 - temp greater than 85° (exclusive)
void tempAboveOperationalRange(float temp){
  if(temp > 85.0){
    Serial.println(F("Temperature has exceeded 85° C"));
    Serial.println(F("Temperature is outside the operational range for the BME680 sensor")); 
  } 
}

//TC11 - temp below 0° (exclusive)
void tempBelowAccuracyRange(float temp){
  if(temp < 0.0){
    Serial.println(F("Temperature is below 0° C"));
    Serial.println(F("Temperature is outside the full accuracy range for the humidity and pressure sensors")); 
  } 
}

//TC12 - temp below -40° (exclusive)
void tempBelowOperationalRange(float temp){
  if(temp < -40.0){
    Serial.println(F("Temperature is below -40° C"));
    Serial.println(F("Temperature is outside the operational range for the BME680")); 
  } 
}

//TC13 - humidity between 10% and 90% (inclusive)
void humidityInRange(float humidity){
  if(humidity >= 10.0 && humidity <= 90.0){
    Serial.println(F("Humidity is within the full accuracy range for the humidity sensor"));  
  } 
}

//TC14 - humidity greater than 90% (exclusive)
void humidityAboveAccuracyRange(float humidity){
  if(humidity > 90.0){
    Serial.println(F("Humidity has exceeded 90% rh"));
    Serial.println(F("Humidity is outside the full accuracy range for the humidity sensor")); 
  } 
}

//TC15 - humidity greater than 95% (exclusive)
void humidityAboveOperationalRange(float humidity){
  if(humidity > 95.0){
    Serial.println(F("Humidity has exceeded 95% rh"));
    Serial.println(F("Humidity is outside the operational range for the gas sensor")); 
  } 
}

//TC16 - humidity below 10% (exclusive)
void humidityBelowOperationalRange(float humidity){
  if(humidity < 10.0){
    Serial.println(F("Humidity is below 10% rh"));
    Serial.println(F("Humidity is outside the operational range for the gas sensor")); 
  } 
}

//TC17 - pressure between 8.85899 and 32.48298 (inclusive)
void pressureInRange(float pressure){
  if(pressure >= 8.85899 && pressure <= 32.48298){
    Serial.println(F("Pressure is within the full accuracy range for the pressure sensor"));  
  }  
}

//TC18 - pressure less than 8.85899 (exclusive)
void pressureBelowAccuracyRange(float pressure){
  if(pressure < 8.85899){
    Serial.println(F("Pressure is below 8.85899 inHg"));
    Serial.println(F("Pressure is outside the full accuracy range for the pressure sensor")); 
  } 
}

//TC19 - pressure greater than 32.48298 (exclusive)
void pressureAboveAccuracyRange(float pressure){
  if(pressure > 32.48298){
    Serial.println(F("Pressure has exceeded 32.48298 inHg"));
    Serial.println(F("Pressure is outside the full accuracy range for the pressure sensor")); 
  } 
}
