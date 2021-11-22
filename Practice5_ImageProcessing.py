import cv2 
     
image = cv2.imread('oveisi.jpg', 0)
print(image.shape)

start_point = (50, 0)
end_point = (0, 50)
color = (0, 0, 0)
thickness = 8
image = cv2.line(image, start_point, end_point, color, thickness)   
cv2.imshow('Fathali Oveisi Rohat Shad', image) 
cv2.waitKey(0)
