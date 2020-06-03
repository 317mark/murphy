"""
Script to be run at startup
"""

# Imports
import RPi.GPIO as GPIO


# Set pin numbering schema
GPIO.setmode(GPIO.BCM)


# Boot Script
# Put rocket in Idle mode

# Make connection with Arduino

# Calibrate/Test sensors

# Turn on the camera, begin recording, and create file to be saved to

# Indicate that sensors are reading out and properly calibrated (LED + Sound)

# Create flight data file on SD card, and begin logging sensor output to it

# Make connection with Controller Box

# Wait for further instructions

# If controller dial is set to Arm, arm the rocket

# If controller dial is set to Arm && the flip is switched, launch the rocket
