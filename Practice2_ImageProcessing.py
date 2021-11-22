import cv2

img=cv2.imread('1.jpg',0)
height,width=img.shape
for i in range(height):
    for j in range(width):
        img[i,j]=255-img[i,j]

cv2.imshow('CR7',img)
cv2.imwrite('1_res.jpg',img)

cv2.waitKey()
