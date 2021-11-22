import cv2
imgage = cv2.imread('wolf_picture.jpg', 0)
h,w = imgage.shape
a=120
for i in range(h):
    for j in range(w):
        if imgage[i][j]<a:
            imgage[i][j] = 255-a
# cv2.imwrite('Wolf_Split_pic.png', imgage)
cv2.imshow('Wolf_Split_Picture',imgage)
cv2.waitKey(0)