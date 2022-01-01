import cv2

img = cv2.imread("D:\\Python Project\\python_programming\\tamrin9\\Carrot.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w, _ = img.shape
print("pixel", h,w)

R, G, B = cv2.split(img)

R_new = G
G_new = G
B_new = R


new_img = cv2.merge((B_new, G_new, R_new))
result = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
