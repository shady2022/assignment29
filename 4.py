import numpy as np
import cv2

  
# taking the input from webcam
vid = cv2.VideoCapture(0)
  
# running while loop just to make sure that
# our program keep running untill we stop it
while True:
  
    # capturing the current frame
    ret, frame = vid.read()
    width = int(vid.get(3))
    height = int(vid.get(4))
    
    bgr =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #if  0 < np.average(color_detection_area) <= 60:
        #cv2.putText(dst, "Black", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 
    #elif 70 < np.average(color_detection_area) <= 120:
       # cv2.putText(dst, "Gray", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    #else:
        #cv2.putText(dst, "White", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 

    B, G, R = cv2.split(bgr)
    
    B_new = int(np.average(B))
    G_new = int(np.average(G))
    R_new = int(np.average(R))
    print(B_new, G_new, R_new)
    
    
  
    # displaying the most prominent color
    if (B_new > G_new and B_new > R_new):
        print("Blue")
    if (G_new > R_new and G_new > B_new):
        print("Green")
    elif(R_new > B_new and R_new > G_new):
        print("Red")
        
    elif ((B_new>=0 and B_new<=70) and (G_new>=0 and G_new<=70) and (R_new>=90 and R_new<=255)):
            cv2.putText(frame,'Red',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 

    elif ((B_new>=100 and B_new<=255) and (G_new>=0 and G_new<=100) and (R_new>=0 and R_new<=100)):
        cv2.putText(frame,'Blue',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA) 

    elif ((B_new>=0 and B_new<=50) and (G_new>=50 and G_new<=255) and (R_new>=0 and R_new<=50)):
        cv2.putText(frame,'Green',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5,cv2.LINE_AA)    
   

    elif((B_new>=50 and B_new<=100) and (G_new>=35 and G_new<=45) and (R_new>=50 and R_new<=100)):   
        cv2.putText(frame,'Purple',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 

    elif((B_new>=130 and B_new<=255) and (G_new>=130 and G_new<=255) and (R_new>=130 and R_new<=255)):   
        cv2.putText(frame,'White',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 

    elif((B_new>=0 and B_new<=50) and (G_new>=0 and G_new<=30) and (R_new>=0 and R_new<=30)):   
        cv2.putText(frame,'Black',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA)    

    elif((B_new>=65 and B_new<=95) and (G_new>=65 and G_new<=95) and (R_new>=65 and R_new<=95)):
        cv2.putText(frame,'Gray',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 
    
    elif((B_new>=190 and B_new<=255) and (G_new>=190 and G_new<=255) and (R_new>=0 and R_new<=150)):
        cv2.putText(frame,'Cyan',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA) 

    elif((B_new>=0 and B_new<=70) and (G_new>=75 and G_new<=255) and (R_new>=75 and R_new<=255)):
        cv2.putText(frame,'Yellow',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),5,cv2.LINE_AA)       
        
        
        
    
   
    cv2.imshow('Camera',frame)
    if  cv2.waitKey(1) == ord("q"):
        break
vid.release()
#cv2.waitKey(1)
cv2.destroyAllWindows()