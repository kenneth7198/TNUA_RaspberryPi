from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (640, 480)
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    camera.capture('/home/pi/Desktop/colorEffect%s.jpg' % effect)
    sleep(2)
camera.stop_preview()
