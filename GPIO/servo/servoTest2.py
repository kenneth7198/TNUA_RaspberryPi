import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servoPin = 21

GPIO.setup(servoPin, GPIO.OUT)
servo1 = GPIO.PWM(servoPin, 50)
servo1.start(2.5) #0

while True:
    servo1.ChangeDutyCycle(12.5)  #180
    time.sleep(2)
    servo1.ChangeDutyCycle(2.5)   #0
    time.sleep(2)
    servo1.ChangeDutyCycle(7.5)   #90
    time.sleep(2)
    

    
