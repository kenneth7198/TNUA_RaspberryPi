import SimpleCV
import time

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    blobs = img.findBlobs()
    img.crop(blobs[-1])
    img.show()
