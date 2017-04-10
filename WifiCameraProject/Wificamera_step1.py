from picamera import PiCamera
from time import sleep
import RPi.GPIO as io

camera = PiCamera()
inputButtonPin = 21
imgCounter = 0

io.setmode(io.BCM)
io.setup(inputButtonPin, io.IN)

while True:
    value = io.input(inputButtonPin)
    #print(value)
    if value == 0:
        print("You pressed shot button!")
        camera.start_preview()
        sleep(0.5)
        camera.stop_preview()
        camera.capture('/home/pi/Pictures/DCM_image_%s.jpg' % imgCounter)
        imgCounter += 1
        while value == 0:
            value = io.input(inputButtonPin)
            


   
