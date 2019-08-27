import numpy as np
import cv2
cap=cv2.VideoCapture(0)
length=0
lengths=[]
n=0
while True:
    _,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue=np.array([105,150,70])
    upper_blue=np.array([120,255,255])
    
    '''frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(frame_gray,130,255,0)
    cv2.imshow('thersh',thresh)'''
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    mask=cv2.medianBlur(mask,15)
    
    cv2.imshow("mask",mask)
    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(len(contours)!=0):
        cnt = max(contours, key = cv2.contourArea)
        cv2.drawContours(frame, [cnt], 0, (0,0,255), 3)
        x,y,w,h = cv2.boundingRect(cnt)
                    
        if(w>h):
            length=(w/h)*3.2
        else:
            length=(h/w)*3.2
        '''lengths.append(length)
        length=np.mean(lengths)'''
        print(length)    
        cv2.imshow("contours",frame)
    else:
        continue
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()

    
