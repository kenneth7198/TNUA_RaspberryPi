import SimpleCV

cam = SimpleCV.Camera()
windowsSize = (640,480)
disp = SimpleCV.Display(windowsSize)

while disp.isNotDone():
    img = cam.getImage()
    corner = [(0,0),(640,0),(640,480),(50,480)] #x1,y1 x2,y2 x3,y3 x4,y4
    sw = img.shear(corner)
    sw.show()
