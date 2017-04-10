import RPi.GPIO as GPIO
import time

relay1=13
relay2=12
relay3=11
relay4=10

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)

while True:
    GPIO.output(relay1,True)
    time.sleep(1)
    GPIO.output(relay1,False)
    time.sleep(1)
    GPIO.output(relay2,True)
    time.sleep(1)
    GPIO.output(relay2,False)
    time.sleep(1)
    GPIO.output(relay3,True)
    time.sleep(1)
    GPIO.output(relay3,False)
    time.sleep(1)
    GPIO.output(relay4,True)
    time.sleep(1)
    GPIO.output(relay4,False)
    time.sleep(1)
