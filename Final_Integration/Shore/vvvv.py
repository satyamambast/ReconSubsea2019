import cv2
import numpy as np
from Task_Shape_Detection.Shape_Detection import shape
#from Task_Crack_Detection.crackmeasurement import crack
#from Task_Character_Detection.detect2 import *

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    #cv2.imshow('frame',frame)
    shape(frame)
    #crack(frame)
    #feed()
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
