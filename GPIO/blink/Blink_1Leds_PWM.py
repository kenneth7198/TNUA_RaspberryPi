import RPi.GPIO as GPIO
import time

led1=17

delayTime = 0.05

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

pwm1 = GPIO.PWM(led1, 50)  #50Hz
pwm1.start(0)              #Start from 0 to 100

while True:
    for i in range(0,101):
        pwm1.ChangeDutyCycle(i)
        time.sleep(delayTime)

    for i in range(100,-1,-1):
        pwm1.ChangeDutyCycle(i)
        time.sleep(delayTime)
    
    
