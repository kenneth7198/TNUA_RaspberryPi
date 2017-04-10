import picamera
import time

camera = picamera.PiCamera()
camera.resolution=(640,480)
camera.framerate=30
camera.ISO = 200
time.sleep(2)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g


for i in range(0, 10):
    camera.start_preview()
    time.sleep(0.5)
    
    camera.capture('img%s.jpg' % i)
    camera.stop_preview()
    time.sleep(0.5)
