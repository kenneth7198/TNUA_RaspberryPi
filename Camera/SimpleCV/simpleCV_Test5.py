from SimpleCV import Camera

cam = Camera()

while True:
    cam = cam.getImage()
    faceDatabase = cam.findHaarFeatures("face.xml")

    for f in faceDatabase:
        print "Found a face at" + str(f.coordinates())

    green = (0,255,0)

    faceDatabase.sortColorDistance(green)[0].draw(green)
    cam.save("face_detected.jpg")
