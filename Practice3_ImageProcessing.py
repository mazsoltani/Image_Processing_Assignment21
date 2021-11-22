import cv2

img = cv2.imread('sad.jpg', 0)
image = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('Rotate Picture', image)
cv2.waitKey()       

