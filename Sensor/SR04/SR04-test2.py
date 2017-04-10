import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 21
GPIO_ECHO = 20
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

while True:
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001) #10uS
    GPIO.output(GPIO_TRIGGER, False)
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = TimeElapsed * 17150
    #distance = round(distance, 3)
  
    if distance >2 and distance < 400:
        print ("Measured Distance = %.1f cm" % distance)
        
    time.sleep(0.05) #50mS

