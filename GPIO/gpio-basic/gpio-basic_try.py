import RPi.GPIO as GPIO
import time
import sys

led=11

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, True)
    time.sleep(1)
    GPIO.output(led, False)
    time.sleep(1)
