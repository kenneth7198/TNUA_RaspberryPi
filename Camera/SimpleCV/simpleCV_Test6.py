from SimpleCV import *
import time

cam = Camera()
display = Display()

haarcascade = HaarCascade("face.xml")

while display.isNotDone():
    image = cam.getImage().scale(0.5)
    faces = image.findHaarFeatures(haarcascade)
    if faces:
        face = faces[-1]
        face.draw(Color.RED, 1)

    image.show()
