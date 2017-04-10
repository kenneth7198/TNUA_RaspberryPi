from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
camera.image_effect = 'colorswap'
sleep(2)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()
