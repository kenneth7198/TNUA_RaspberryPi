from SimpleCV import *
import time

#cam = Camera(0, {"width":160,"height":120})
cam = Camera()
cam.live()
winsize = (160,120)
display = Display(winsize)
size = cam.getImage().size()
center = (size[0] /2, size[1] /2)
print(size)

#haarcascade = HaarCascade("face.xml")
haarcascade = HaarCascade("face.xml")

while display.isNotDone():
    img = cam.getImage()
    #scalesize = 0.5
    #scaledimg = img.scale(scalesize)
    
    faces = img.findHaarFeatures(haarcascade)

    #if faces:
    #    face = faces[-1]
    #    

    #image.show()
    if faces:
        face = faces[-1]
        face.draw(Color.RED, 1)
        #img.show(type="browser")
       
        print("x= "+ str(face.x) + "y= "+ str(face.y))

        

    else:
        print("no face")

    img.show()

#time.sleep(0.1)
