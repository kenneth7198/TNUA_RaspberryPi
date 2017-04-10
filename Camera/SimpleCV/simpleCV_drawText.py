import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display()

while disp.isNotDone():
    img = cam.getImage()
    img.drawText("Hello World!",200,400)
    img.save('img.jpg')
    img.show()
 
