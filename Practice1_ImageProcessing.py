import numpy as np
import cv2

row = 800
col = 800
chessboard=np.zeros((row , col ))

for i in range(row):
    for j in range(col):
        x=(i//100)%2
        y=(j//100)%2

        if (x+y) % 2 ==0 :
            chessboard[i][j]=255
        else:
            chessboard[i][j]=0          

cv2.imwrite('chessboard.jpg',chessboard)
# cv2.imshow("Chess Board" , chessboard) 
cv2.waitKey()