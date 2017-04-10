import SimpleCV
import time

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    for i in range(0,360):
        rot = img.rotate(i, scale=0.5)
        rot.show()
        time.sleep(0.1)
