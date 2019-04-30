import cv2
import numpy as np
from Task_Shape_Detection.Shape_Detection import shape
#from Task_Crack_Detection.crackmeasurement import crack
from Task_Character_Detection.detect2 import *

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    #detect(frame)
    #cv2.imshow('frame',frame)
    s,f=shape(frame)
    #crack(frame)
    #feed()
    cv2.imshow('frames',f)
    print(s)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    

