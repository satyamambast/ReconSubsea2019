import numpy as np
import cv2
import sys
import pytesseract

config = ('-l eng --oem 1 --psm 3')
def text_detection(ret,frame):
    print(ret)
    text = pytesseract.image_to_string(frame, config=config)
    #cv2.imshow('frame',frame)
    print(text)
    
