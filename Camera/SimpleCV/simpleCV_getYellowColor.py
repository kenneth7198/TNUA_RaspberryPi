import SimpleCV

cam = SimpleCV.Camera()
windowsSize = (640,480)
disp = SimpleCV.Display(windowsSize)
cam.live()
distColor = (223,191,29)

while disp.isNotDone():
    img = cam.getImage()
    yellowDist = img.colorDistance(distColor)
    yellowDistBin = yellowDist.binarize()
    yellowDistInv = yellowDistBin.invert()
    yellowDistInv.show()
