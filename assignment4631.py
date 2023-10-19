import numpy as np
import cv2

image=cv2.imread("input/lion.png",1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows,cols=gray.shape
result=np.zeros((rows,cols),dtype=np.uint8)
# filter=np.array([[1,0,5]
#                  ,[0,1, 5]
#                  ,[1, 1, 5 ]])

for i in range (1,rows-1):
    for j in range (1,cols-1):
        small=gray[i-1:i+2,j-1:j+2]
        # average=np.mean(small)
        average=np.sum(filter*small)
        result[i,j]=average
        
cv2.imwrite("output/lion-edge-detection.png",result)