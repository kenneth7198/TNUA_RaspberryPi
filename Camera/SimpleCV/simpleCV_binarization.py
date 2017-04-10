import SimpleCV

cam = SimpleCV.Camera()
windowsSize = (640,480)
disp = SimpleCV.Display(windowsSize)

while disp.isNotDone():
    img = cam.getImage()
    imgBin = img.binarize()
    imgBin.show()
