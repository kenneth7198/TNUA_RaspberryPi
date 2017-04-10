import SimpleCV

cam = SimpleCV.Camera()
windowsSize = (640,480)
disp = SimpleCV.Display(windowsSize)
rotate = 0

while disp.isNotDone():
    rotate += 5
    img = cam.getImage()
    imgR = img.rotate(rotate)
    imgR.show()
