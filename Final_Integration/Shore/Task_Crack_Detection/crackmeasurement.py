import cv2
import io
import struct
import pickle
import numpy as np
import time 
from math import sqrt
from statistics import mode,mean
import socket


def distanceformula(x1,y1,x2,y2):
    return(sqrt((x1-x2)**2 + (y1-y2)**2)) 

def crack(frame):
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))
    crack_length=0
    k=1.5
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([80,100,100])
    upper = np.array([120,250,250])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if len(conts)!=0:
        c=max(conts,key=cv2.contourArea)
        cv2.drawContours(frame,c,-1,(0,0,0),3)
        rect =cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame,[box],0,(0,0,255),2)
        l,b=distanceformula(box[0][0],box[0][1],box[1][0],box[1][1]),distanceformula(box[1][0],box[1][1],box[2][0],box[2][1])
        if l>b:
            crack1=((l/b)*k)
        else:
            crack1=((b/l)*k)
        print(crack1)
        return crack1,frame
    return 0,frame
    #cv2.imshow('crack',frame)
"""c=cv2.VideoCapture(0)
while True:
    _,frame=c.read()
    cracklength,frame1=crack(frame)
    cv2.imshow('f',frame1)
    cv2.waitKey(1)
"""
