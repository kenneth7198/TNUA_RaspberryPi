from SimpleCV import *
import time

cam = Camera()
cam.live()
display = Display((90,90))

#haarcascade = HaarCascade("face.xml")
haarcascade = HaarCascade("eye.xml")

while display.isNotDone():
    img = cam.getImage()
    scalesize = 0.5
    scaledimg = img.scale(scalesize)
    
    faces = img.findHaarFeatures(haarcascade)

    #if faces:
    #    face = faces[-1]
    #    

    #image.show()
    if faces:
        face = faces[-1]
        face.draw(Color.RED, 1)
        img.show()
        print("x= "+ str(face.x) + "y= "+ str(face.y))

        

    else:
        print("no face")


time.sleep(0.1)
