import SimpleCV

cam = SimpleCV.Camera()
windowsSize = (640,480)
disp = SimpleCV.Display(windowsSize)
frameWeight = 0.1
lastImg = cam.getImage()
    
while disp.isNotDone():
    img = cam.getImage()
    img = (img * frameWeight) + (lastImg * (1 - frameWeight))
    img.show()
    lastImg = img
