import RPi.GPIO as GPIO
import time

relayPin = [13,12,11,10,9,8,7]

GPIO.setmode(GPIO.BCM)
for i in range(0,7):
    GPIO.setup(relayPin[i], GPIO.OUT)

while True:
    for i in range(0,7):
        GPIO.output(relayPin[i],True)
        time.sleep(1)
        GPIO.output(relayPin[i],False)
        time.sleep(1)
