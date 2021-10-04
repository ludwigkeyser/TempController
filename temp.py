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

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)

interval = 5
targetTemp = 25.5
variance = 1
heatingIndicator = "off"

while True:
    tempNow = max31855.temperature
    
    timeNow = datetime.now()
    timestampStr = timeNow.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    f = open('templog.csv', 'a')
    f.write(timestampStr + ', ' + str(tempNow) + ', ' + heatingIndicator + '\n')
    f.close()

    if tempNow < targetTemp - (variance / 2):
        if GPIO.input(GPIOChannel) == 0:
            GPIO.output(GPIOChannel, GPIO.HIGH) #turn heating on
            heatingIndicator = "on"
    
    if tempNow >= (targetTemp + variance / 2):
        if GPIO.input(GPIOChannel) == 1:
            GPIO.output(GPIOChannel, GPIO.LOW) #turn heating off
            heatingIndicator = "off"

    time.sleep(interval)



