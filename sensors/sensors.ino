#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>

/* BMP280 Barometric Pressure Sensor Requirements */
#include <Adafruit_BMP280.h>
#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11
#define BMP_CS 10
Adafruit_BMP280 bmp; // I2C

/* BNO055 Orientation Sensor Requirements */
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)
Adafruit_BNO055 bno = Adafruit_BNO055(55);

/* ADXL377 Accelerometer Requirements */
#include "ADXL335.h"
ADXL335 accelerometer;

const int buttonPin = 13;
int buttonState = HIGH;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);

  bmp.begin();
  accelerometer.begin();
  bno.begin();

  pinMode(buttonPin, INPUT);
}

void loop()
{
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    sensors_event_t event;
    bno.getEvent(&event);
  
    /* Display the floating point data */
    Serial.print("X: ");
    Serial.print(event.orientation.x, 4);
    Serial.print(" Y: ");
    Serial.print(event.orientation.y, 4);
    Serial.print(" Z: ");
    Serial.print(event.orientation.z, 4);
    Serial.print("\tTemp: ");
    Serial.print(bmp.readTemperature() * 1.8 + 32);
    Serial.print(" F");
    Serial.print("\tAltitude: ");
    Serial.print(bmp.readAltitude(1013.25) * 3.208084);
    Serial.println(" ft");
  
    delay(100);
  }
}
