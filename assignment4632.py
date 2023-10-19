import numpy as np
import cv2

image=cv2.imread("input/spider.webp",1)
# type(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows,cols=gray.shape
# result=np.zeros((rows,cols),dtype=np.uint8)
# filter=np.array([[1,0,5]
#                  ,[0,1, 5]
#                  ,[1, 1, 5 ]])

# # filter=np.ones((3,3))/9
edge=cv2.Canny(gray,50,110)
# for i in range (1,rows-1):
#     for j in range (1,cols-1):
#         small=gray[i-1:i+2,j-1:j+2]
#         # average=np.mean(small)
#         average=np.sum(filter*small)
#         result[i,j]=average
        
cv2.imwrite("output/spider-edge-detection.png",edge)