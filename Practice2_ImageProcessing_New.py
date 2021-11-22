import numpy
import cv2

img = cv2.imread('1.jpg')
convert_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('CR7',img)
cv2.imwrite('1_res.png',convert_image )

cv2.waitKey()

# باکمک از سایت زیر
# https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/