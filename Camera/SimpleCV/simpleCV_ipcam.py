import SimpleCV

#cam = SimpleCV.Camera()
ipcam = SimpleCV.JpegStreamCamera("http://192.168.43.204:8080/")
disp = SimpleCV.Display()

while disp.isNotDone():
    img = ipcam.getImage()
    img.show()
