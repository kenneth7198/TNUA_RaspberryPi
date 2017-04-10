import SimpleCV

loadVideo = SimpleCV.VirtualCamera("test.mp4","video")
disp = SimpleCV.Display()

while disp.isNotDone():
    img = loadVideo.getImage()
    img.show()
    
