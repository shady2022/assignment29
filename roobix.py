import matplotlib.pyplot as plt
import cv2

img_rubic_BGR=cv2.imread('D:\\Python Project\\python_programming\\tamrin9\\rubix.png')
img_rubic_RGB=cv2.cvtColor(img_rubic_BGR,cv2.COLOR_BGR2RGB)
cv2.imshow("new",img_rubic_RGB)

B,G,R=cv2.split(img_rubic_BGR)
rows,cols,_=img_rubic_BGR.shape

for i in range(rows):
    for j in range(cols):
        if R[i,j]==0 and B[i,j]==255 and G[i,j]==255:
            img_rubic_RGB[i-3:i+3,j-3:j+3]=(255,0,0)
        if R[i,j]==255 and B[i,j]==0 and G[i,j]==255:
            img_rubic_RGB[i-3:i+3,j-3:j+3]=(0,0,255)

        if R[i,j]==255 and B[i,j]==255 and G[i,j]==0:
            img_rubic_RGB[i-3:i+3,j-3:j+3]=(0,255,0)

cv2.imwrite('rubic.jpg',img_rubic_RGB)
plt.imshow(img_rubic_RGB)