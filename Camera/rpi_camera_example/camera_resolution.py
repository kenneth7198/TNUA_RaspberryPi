from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (64, 64)
camera.framerate = 15
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/test.jpg')
camera.stop_preview()
