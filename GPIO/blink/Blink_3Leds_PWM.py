import RPi.GPIO as GPIO
import time

ledPins = [17,27,22]

delayTime = 0.01

GPIO.setmode(GPIO.BCM)

for i in range(0,3):
    GPIO.setup(ledPins[i], GPIO.OUT)

pwm1 = GPIO.PWM(ledPins[0], 50)
pwm2 = GPIO.PWM(ledPins[1], 50)
pwm3 = GPIO.PWM(ledPins[2], 50)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

    
while True:
    for i in range(0,101):
        pwm1.ChangeDutyCycle(i)
        pwm2.ChangeDutyCycle(i)
        pwm3.ChangeDutyCycle(i)
        time.sleep(delayTime)

    for i in range(100,-1,-1):
        pwm1.ChangeDutyCycle(i)
        pwm2.ChangeDutyCycle(i)
        pwm3.ChangeDutyCycle(i)
        time.sleep(delayTime)
    
