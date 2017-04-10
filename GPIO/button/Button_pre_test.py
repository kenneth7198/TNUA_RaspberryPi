import RPi.GPIO as GPIO

inputButton=10

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputButton, GPIO.IN)

while True:
    value = GPIO.input(inputButton)
    print(value)
    
