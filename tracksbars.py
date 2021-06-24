import cv2
import numpy as np
import cv2 as cv

#create black image using a window
#img = np.zeros((300,512,3),np.uint8)

def nothing(x):
    print(x)

cv.namedWindow('image')

cv.createTrackbar('CP','image',10,400,nothing)
#cv.createTrackbar('G','image',0,255,nothing)
#cv.createTrackbar('R','image',0,255,nothing)

switch = 'color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)
while(1):
    img = cv.imread('kid.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(50,150),font,5,(0,0,255),6)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv.getTrackbarPos(switch,'image')
    if s==0:
        pass
    else:
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    img = cv.imshow('image',img)
    #g = cv.getTrackbarPos('G','image')
    #r = cv.getTrackbarPos('R','image')
    #s = cv.getTrackbarPos(switch,'image')

cv.destroyAllWindows()
