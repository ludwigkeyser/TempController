import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

relay_one_status = GPIO.input(17)  # Returns 0 if OFF or 1 if ON
relay_two_status = GPIO.input(18)

if relay_one_status ==  0: 
   print("Relay 1 status: off")
else:
   print("Relay 1 status: on")

if relay_two_status == 0:
   print("Relay 2 status: off")
else:
   print("Relay 2 status: on")


