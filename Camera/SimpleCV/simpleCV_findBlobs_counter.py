import SimpleCV

cam = SimpleCV.Camera(0,{"width":320,"height":240})
disp = SimpleCV.Display((320,240))

while disp.isNotDone():
    img = cam.getImage()
    p = img.scale(320,240)
    b = p.findBlobs(minsize=20,maxsize=300)
    if b:
        b.draw((255,0,0))
        print("Blobs:"+str(b.count()))

    p.show()
    
