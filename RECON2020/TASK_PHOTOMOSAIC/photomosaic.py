import cv2
import numpy as np
import imutils
photomosaic1=cv2.imread("photomosaic1.png")
photomosaic2=cv2.imread("photomosaic2.png")

photomosaic3=cv2.imread("photomosaic3.png")

photomosaic4=cv2.imread("photomosaic4.png")
photomosaic5=cv2.imread("photomosaic5.png")
white=cv2.imread("white.jpg")

shape1=photomosaic1.shape
shape2=photomosaic2.shape
shape3=photomosaic3.shape
shape4=photomosaic4.shape
shape5=photomosaic5.shape


photomosaic1=cv2.resize(photomosaic1,(500,200))
photomosaic2=cv2.resize(photomosaic2,(500,200))
photomosaic3=cv2.resize(photomosaic3,(500,200))
photomosaic4=cv2.resize(photomosaic4,(500,200))
photomosaic5=cv2.resize(photomosaic5,(500,200))


d={1:abs(shape1[0]-shape1[1]),2:abs(shape2[0]-shape2[1]) ,3:abs(shape3[0]-shape3[1]),4:abs(shape4[0]-shape4[1]),5:abs(shape5[0]-shape5[1])}
d=sorted(d.items(), key=lambda x: x[1])
print(d[0][0],d[1][0])
if(d[0][0]==1):
    photomosaic1=cv2.resize(photomosaic1,(200,200))
elif(d[0][0]==2):
    photomosaic2=cv2.resize(photomosaic2,(200,200))
elif(d[0][0]==3):
    photomosaic3=cv2.resize(photomosaic3,(200,200))
elif(d[0][0]==4):
    photomosaic4=cv2.resize(photomosaic4,(200,200))


if(d[1][0]==1):
    photomosaic1=cv2.resize(photomosaic1,(200,200))
elif(d[1][0]==2):
    photomosaic2=cv2.resize(photomosaic2,(200,200))
elif(d[1][0]==3):
    photomosaic3=cv2.resize(photomosaic3,(200,200))
elif(d[1][0]==4):
    photomosaic4=cv2.resize(photomosaic4,(200,200))

if(photomosaic4.shape[1]==200):
    
    white=cv2.resize(white,(1400-photomosaic4.shape[1],photomosaic5.shape[1]))
    photomosaic5=cv2.resize(photomosaic5,(200,500))

    
elif(photomosaic4.shape[1]==500):
    white=cv2.resize(white,(1400-photomosaic4.shape[1],photomosaic5.shape[0]))
    photomosaic5=cv2.resize(photomosaic5,(500,200))
    print("WHITE : ",white.shape)
    

    
    
    

shape1=photomosaic1.shape
shape2=photomosaic2.shape
shape3=photomosaic3.shape
shape4=photomosaic4.shape
shape5=photomosaic5.shape    
print(d)


print(shape1)
print(shape2)
print(shape3)
print("SHAPE : ",shape4)
print(shape5)



#print("white",white.shape," ",photomosaic5.shape)
top=np.column_stack((white,photomosaic5))
base=np.column_stack((photomosaic1,photomosaic2,photomosaic3,photomosaic4))
final=np.row_stack((top,base))

print(top.shape,base.shape)
print("TYPE ",type(base),type(top))

cv2.imshow("final",final)


cv2.waitKey(0)
cv2.destroyAllWindows()

