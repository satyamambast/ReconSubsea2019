import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue=np.array([105,150,70])
    upper_blue=np.array([120,255,255])

    


    lower_red=np.array([-20,190,70])
    upper_red=np.array([16,255,250])

    
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    mask2=cv2.inRange(hsv,lower_blue,upper_blue)

    mask=mask2+mask1
    res=cv2.bitwise_and(frame,frame,mask=mask)



    median=cv2.medianBlur(res,15)

    bilateral=cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('frame',frame)
    #cv2.imshow('res',res)

    cv2.imshow('median',median)


    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
