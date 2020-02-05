import argparse
import cv2
import numpy as np
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
width=0
height=0
def perspective(w,h):
    pts1 = np.float32(refPt)
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(image1, matrix, (w, h))
    #cv2.imshow("Image", img)
    cv2.imshow("Perspective transformation", result)
    cv2.imwrite("photo5.jpeg",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    
    
    print("HELLO")
def click_and_crop(event, x, y, flags, param):
    global refPt
    image1=image
	
    if(event == cv2.EVENT_LBUTTONDOWN):
        refPt.append([x,y])
        cv2.circle(image, (x,y), 5, (0, 0, 255), -1)
        print(refPt)
        if(len(refPt)==4):
            width=abs(refPt[0][0]-refPt[1][0])
            height=abs(refPt[0][1]-refPt[2][1])
            print(height,width)
            perspective(width,height)
		
 
	
    
image = cv2.imread('5.jpeg')
image=cv2.resize(image,(480,640))

image1=cv2.imread('5.jpeg')
image1=cv2.resize(image1,(480,640))

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
while True:
	
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
         
	
 

 
# close all open windows
cv2.destroyAllWindows()
