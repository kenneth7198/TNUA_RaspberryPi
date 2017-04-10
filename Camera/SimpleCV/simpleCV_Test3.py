from operator import add
from SimpleCV import *

cam = Camera()

frames_to_blur = 10
frames = ImageSet()

while True:
    frames.append(cam.getImage())

    if len(frames) > frames_to_blur:
        frames.pop(0)

    pic = reduce(add, [i / float(len(frames)) for i in frames])

    pic.show()
