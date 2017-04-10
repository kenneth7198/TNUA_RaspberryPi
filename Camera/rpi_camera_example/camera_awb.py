from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
camera.awb_mode = 'sunlight'
camera.capture('/home/pi/Desktop/sunlight.jpg')
sleep(2)
camera.stop_preview()
