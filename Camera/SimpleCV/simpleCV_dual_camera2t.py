from SimpleCV import *

cam1 = Camera(0)
#cam2 = Camera(0)
disp1 = Display((320,240),0,'Dual Camera')

haar = HaarCascade("face4.xml")
txt=""

imgText = DrawingLayer((320,240))

        
while disp1.isNotDone():
    img1 = cam1.getImage().resize(80,60)
    #img2 = cam2.getImage().resize(160,120).binarize()
    #img2 = cam2.getImage().resize(80,60)

    faces = img1.findHaarFeatures(haar)

    if faces:
        face = faces[-1]
        #face.draw(Color.RED, 1)
        print("x="+str(face.x)+"y="+str(face.y))
        txt = "Face position x= " + str(face.x) + " y= "+str(face.y)
        #img1.drawText(txt)
        #img1.blit(imgText)
        
        
                
    else:
        print("There is no face in img1.")

    imgText.text("t",(100,100))
    img1.addDrawingLayer(imgText)
    disp1.writeFrame(img1)
    
    #disp1.writeFrame(imgText)

        
    #allInOne = img1.sideBySide(img2)
    #disp1.writeFrame(allInOne)    
    
