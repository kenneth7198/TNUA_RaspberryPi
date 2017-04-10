from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
camera.brightness = 30
camera.annotate_text = "Hi Raspberry Pi"
sleep(3)
camera.capture('/home/pi/Desktop/brightness.jpg')
camera.stop_preview()
