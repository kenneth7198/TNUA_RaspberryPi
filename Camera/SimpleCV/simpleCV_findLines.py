import SimpleCV

cam = SimpleCV.Camera(0,{"width":320,"height":240})
disp = SimpleCV.Display((320,240))

while disp.isNotDone():
    img = cam.getImage()
    lines = img.findLines(threshold=1,minlinelength=50)
    lines.draw((255,0,0),width=3)
    img.show()
    
