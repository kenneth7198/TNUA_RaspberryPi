import SimpleCV

cam = SimpleCV.Camera(0,{"width":320,"height":240})
disp = SimpleCV.Display((320,240))

while disp.isNotDone():
    img = cam.getImage()
    circles = img.findCircle()
    #circles = circles.sortArea()
    circles.draw()
    #circles[0].draw((0,255,0),width=3)
    #circles[1].draw((255,0,0),width=2)
    img.show()
