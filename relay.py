import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

interval = 10

time.sleep(interval)

GPIO.output(17, GPIO.HIGH)
time.sleep(interval)
GPIO.output(17, GPIO.LOW)

GPIO.output(18, GPIO.HIGH)
time.sleep(interval)
GPIO.output(18, GPIO.LOW)

