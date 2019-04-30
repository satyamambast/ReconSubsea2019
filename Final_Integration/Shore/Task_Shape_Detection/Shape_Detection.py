import cv2
import numpy as np
from shape_detect.shapedetector import ShapeDetector
import imutils
import pickle
import struct

def shape(frame):
    shapesf={'circle':0,'line':0,'triangle':0,'square':0}
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))
    dataset=[]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,0])
    upper = np.array([180,255,40])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,conts,-1,(230,0,0),3)
    sd = ShapeDetector()
    for c in conts:
        shape = sd.detect(c)
        shapesf[shape]+=1
    return shapesf,frame      
    #cv2.imshow('frame',frame)
    
