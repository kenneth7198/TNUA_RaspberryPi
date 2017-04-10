import RPi.GPIO as GPIO
import time

led1=13
led2=12
led3=11

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

while True:
    GPIO.output(led1, True)
    time.sleep(1)
    GPIO.output(led1, False)
    time.sleep(1)
    
    GPIO.output(led2, True)
    time.sleep(2)
    GPIO.output(led2, False)
    time.sleep(2)

    GPIO.output(led3, True)
    time.sleep(0.5)
    GPIO.output(led3, False)
    time.sleep(0.5)
    
