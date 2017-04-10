import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    if disp.mouseLeft:
        img.dl().circle((disp.mouseX,disp.mouseY), 4, SimpleCV.Color.WHITE, filled=True)
        img.show()
