from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
for i in range(100):
    camera.contrast = i
    camera.annotate_text = "Hi Raspberry Pi! Contrast is : %s" % i
    sleep(0.1)
camera.stop_preview()
