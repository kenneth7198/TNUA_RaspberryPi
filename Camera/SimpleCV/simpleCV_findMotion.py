import SimpleCV

cam = SimpleCV.Camera()
windowsSize = (320,240)
previous = cam.getImage()
disp = SimpleCV.Display(windowsSize)
    
while disp.isNotDone():
    current = cam.getImage()
    motion = current.findMotion(previous)
    for m in motion:
        m.draw((255,0,0),normalize=False)
		
    current.show()
    previous = current
