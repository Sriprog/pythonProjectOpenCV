import cv2
from datetime import datetime
cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1280)
cap.set(4,720)
x =(cap.get(3))
y =(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out =cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width:" + str(x) + " Height:" + str(y)
        date = str(datetime.now())

        frame = cv2.putText(frame,date,(10,50),font,1,
                            (0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()