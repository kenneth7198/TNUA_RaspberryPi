import RPi.GPIO as GPIO
import time

relay1=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)

while True:
    GPIO.output(relay1,True)
    time.sleep(1)
    GPIO.output(relay1,False)
    time.sleep(1)
