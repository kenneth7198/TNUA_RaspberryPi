import RPi.GPIO as GPIO

inputButton1=10
inputButton2=9
inputButton3=8

led1=13
led2=12
led3=11

counter=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputButton1, GPIO.IN)
GPIO.setup(inputButton2, GPIO.IN)
GPIO.setup(inputButton3, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

while True:
    value1 = GPIO.input(inputButton1)
    value2 = GPIO.input(inputButton2)
    value3 = GPIO.input(inputButton3)
    
    GPIO.output(led1, False)
    GPIO.output(led2, False)
    GPIO.output(led3, False)
    
    if value1 == False:
        GPIO.output(led1, True)
        while value1 == False:
            value1 = GPIO.input(inputButton1)
            
    elif value2 == False:
        GPIO.output(led2, True)
        while value2 == False:
            value2 = GPIO.input(inputButton2)

    elif value3 == False:
        GPIO.output(led3, True)
        while value3 == False:
            value3 = GPIO.input(inputButton3)
