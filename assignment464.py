import cv2
import numpy as np

img1=cv2.imread("input/building.png",cv2.IMREAD_GRAYSCALE)


rows,cols=img1.shape
result=np.zeros((rows,cols),dtype=np.uint8)


filter=np.array([[-1 ,0, 1],
                 [-2, 0, 2],
                 [-1, 0 ,1]])

for i in range(1,rows-1):
    for j in range(1,cols-1):
        small=img1[i-1:i+2,j-1:j+2]
        average=np.abs(np.sum(small*filter))
        result[i,j]=average

cv2.imwrite("output/building_vertical.png",result)