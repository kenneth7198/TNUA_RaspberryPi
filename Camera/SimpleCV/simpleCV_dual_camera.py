from SimpleCV import *

cam1 = Camera(0)
cam2 = Camera(1)
disp1 = Display((640,240),0,'Dual Camera')


while disp1.isNotDone():
    img1 = cam1.getImage().resize(320,240)
    img2 = cam2.getImage().resize(320,240)

    allInOne = img1.sideBySide(img2)
    

    disp1.writeFrame(allInOne)    
