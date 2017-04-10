import RPi.GPIO as GPIO

inputButton=10
counter=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputButton, GPIO.IN)

while True:
    value = GPIO.input(inputButton)
    #print(value)
    if value == False:
        print("You pressed button:"+ str(counter) +" Times.")
        counter+=1
        while value == False:
            value = GPIO.input(inputButton)

