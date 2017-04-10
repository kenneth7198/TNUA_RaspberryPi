import picamera

camera = picamera.PiCamera()

camera.start_preview()
camera.capture('img.jpg')
camera.stop_preview()
