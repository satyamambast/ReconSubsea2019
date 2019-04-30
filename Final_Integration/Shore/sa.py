import cv2
img=cv2.imread("shapes.jpg",cv2.IMREAD_COLOR)
cv2.putText(img, 0, (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), lineType=cv2.LINE_AA) 
cv2.putText(img, 0, (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), lineType=cv2.LINE_AA)
cv2.putText(img, 0, (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), lineType=cv2.LINE_AA)
cv2.putText(img, 0, (100, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), lineType=cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
