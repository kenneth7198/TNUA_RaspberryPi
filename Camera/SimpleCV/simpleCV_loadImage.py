import SimpleCV

disp = SimpleCV.Display()

while disp.isNotDone():
    img1 = SimpleCV.Image('pi.png')
    img2 = SimpleCV.Image("http://simplecv.s3.amazonaws.com/simplecv_lg.png")
    img3 = SimpleCV.Image("logo")
    img2.show()
