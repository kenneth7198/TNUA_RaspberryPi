from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils

# Get user supplied values
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(320, 240))

# allow the camera to warmup
time.sleep(0.1)
lastTime = time.time()*1000.0
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    #print time.time()*1000.0-lastTime," Found {0} faces!".format(len(faces))
    #print (faces.x)
    
    lastTime = time.time()*1000.0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.circle(image, (x+w/2, y+h/2), int((w+h)/3), (255, 0, 0), 1)
        print("x:"+str(x)+" y:"+str(y)+" | w:"+str(w)+" h:"+str(h))
        
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
        
  
        

