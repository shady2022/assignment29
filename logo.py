import cv2
import matplotlib.pyplot as plt
import numpy as np

logo=np.ones((600,1200,3),dtype='uint8')* 100
#cv2.imshow("img", logo)

logo[200:300, 200:300]= (246, 83, 20)
logo[310:410, 200:300]= (0, 161, 241)
logo[200:300, 310:410]= (124, 187, 0)
logo[310:410, 310:410]= (255, 187,0) 

cv2.putText(logo,'Microsoft',(420,300),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),10)
logo =cv2.cvtColor(logo,cv2.COLOR_RGB2BGR)
cv2.imshow("new", logo)

cv2.waitKey(0)
cv2.destroyAllWindows()
