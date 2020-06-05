"""
Boot script for the rocket
"""

# Imports #
###############################
# import RPi.GPIO as GPIO
import os
import time
import csv
# import serial
from datetime import date, datetime
# from Sensors.Camera import camera
from rocket import rocket
# from functions import createFlightFolder, createCSV

# Set pin numbering schema
# GPIO.setmode(GPIO.BCM)

# Flight Setup #
###############################
date = date.today()
time = datetime.now()

# If battery has enough charge, continue. If not, warn user of battery life

# Create folder for this flight, and navigate into it
flightName = rocket.name + '-' + \
    date.strftime('%m.%d.%y') + '-' + time.strftime('%H:%M')
flightPath = './Flights/' + flightName
os.mkdir(flightPath)
os.chdir(flightPath)

# Create CSV file to store raw flight data
createCSV()
with open('rawFlightData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["#", "Status", "accelX", "accelY", "accelZ",
                     "velocity", "altitude", "gyroX", "gyroY", "gyroZ"])

print('Flight - ' + date.strftime('%m.%d.%y') + ' ' + time.strftime('%H:%M'))

# Connect to Arduino #
###############################

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# can arduino be a class? arduino.connect(path, baud, timeout)

# while 1:
#     val = ser.readline().decode('utf-8')
#     parsed = val.split(',')
#     parsed = [x.rstrip() for x in parsed]
#     if(len(parsed) > 2):
#         print(parsed)
print('Connected with Arduino')

# Connect to Controller #
###############################


# Sensors #
###############################
# rocket.calibrateSensors()

# Turn on the camera
# camera.start_preview()
# time.sleep(2)  # gives the camera a couple seconds to get it's bearings

# Calibrate BMP280
# rocket.calibrateSensors()

# Calibrate ADXL377

# Calibrate

# Indicate that sensors are reading out and properly calibrated (LED + Sound)


# Make connection with Controller Box

# Wait for further instructions

# If controller dial is set to Arm, arm the rocket
# rocket.arm()
#   Create folder for the flight
#   Start recording video to new file (&& streaming if possible)
#   Create flight data file on SD card, and begin logging sensor output to it
#   Let owner know that the rocket is armed and ready for launch, or if any errors were encountered

# rocket.launch()
# If controller dial is set to Arm && the flip is switched, launch the rocket


# Considerations #
###########
# If flight never launches or arms, delete the folder
