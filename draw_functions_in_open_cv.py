import numpy as np
import cv2
img = cv2.imread('kid.jpg',1)
#img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(0,0),(200,200),(255,0,0),3)
img = cv2.arrowedLine(img,(0,255),(600,600),(56,147,44),3)
img = cv2.rectangle(img,(384,0),(0,426),(0,0,255),3)
img = cv2.circle(img,(565,565),50,(0,0,255),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(50,400),font,4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow('image',img)

k = cv2.waitKey(0) & 0xFF
if(k==27):
    cv2.destroyAllWindows()
elif k ==ord('s'):
    cv2.imwrite('kid_bw.png',img)
    cv2.destroyAllWindows