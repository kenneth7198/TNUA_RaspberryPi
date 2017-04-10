import RPi.GPIO as GPIO

inputButton=10
led=17
counter=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputButton, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    value = GPIO.input(inputButton)
    #Turn off LED 17
    GPIO.output(led, False)
    if value == False:
        print("You pressed button:"+ str(counter) +" Times.")
        counter+=1
        #Show LED 17
        GPIO.output(led, True)
        while value == False:
            value = GPIO.input(inputButton)
            
