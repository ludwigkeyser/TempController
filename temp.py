import time
from datetime import datetime
import board
import digitalio
import adafruit_max31855

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Broadcom pin-numbering scheme

GPIOChannel = 18

GPIO.setup(GPIOChannel, GPIO.OUT) #set Relay 1 output
GPIO.output(GPIOChannel,GPIO.LOW) #set Relay to open (off) for a clean start 

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)

interval = 5
targetTemp = 25.5
variance = 1
heatingIndicator = "stable"

while True:
    # Read the current temperature
    tempNow = max31855.temperature
    
    # Write the current temp to the logfile
    # TODO: Add an option for the logfile name and location
    timeNow = datetime.now()
    timestampStr = timeNow.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    f = open('templog-' + timeNow.strftime("%d-%b-%Y") + ".csv", 'a')
    f.write(timestampStr + ', ' + str(tempNow) + ', ' + heatingIndicator + '\n')
    f.close()

    # If the measured temp is below the target temp + (1/2 the variance), turn the relay on
    if tempNow < targetTemp - (variance / 2):
        if GPIO.input(GPIOChannel) == 0: # Function returns 0 if relay is off
            GPIO.output(GPIOChannel, GPIO.HIGH) #turn heating on
            heatingIndicator = "heating"
    
    
    if tempNow >= (targetTemp + variance / 2):
        if GPIO.input(GPIOChannel) == 1: # Function returns 1 if relay is on
            GPIO.output(GPIOChannel, GPIO.LOW) #turn heating off
            heatingIndicator = "stable"

    time.sleep(interval)



