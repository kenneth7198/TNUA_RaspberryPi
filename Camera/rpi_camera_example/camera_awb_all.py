from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
for awb in camera.EXPOSURE_MODES:
    camera.exposure_mode = awb
    camera.annotate_text = "Exposure: %s" % awb
    camera.capture('/home/pi/Desktop/exposure%s.jpg' % awb)
    sleep(2)
camera.stop_preview()
