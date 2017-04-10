from picamera import PiCamera
from time import sleep
import time
import RPi.GPIO as io

camera = PiCamera()
camera.resolution = (640, 480) #resize resolution

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
        #camera effect
        camera.image_effect = 'watercolor'
        '''
        negative,
        solarize,
        sketch,
        denoise,
        emboss,
        oilpaint,
        hatch,
        gpen,
        pastel,
        watercolor,
        film,
        blur,
        saturation,
        colorswap,
        washedout,
        posterise,
        colorpoint,
        colorbalance,
        cartoon,
        deinterlace1,
        deinterlace2
        '''
        sleep(0.5)
        camera.stop_preview()

        print time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
        timeStamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
        camera.capture('/home/pi/Pictures/DCM_image_%s.jpg' % timeStamp)
        
        while value == 0:
            value = io.input(inputButtonPin)
            


   
