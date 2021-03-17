import cv2
import numpy as np

ball_color = 'blue'

color_dist = {'red': {'Lower': np.array([3, 125, 75]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'yellow': {'Lower': np.array([26, 43, 46]), 'Upper': np.array([34, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              'pink': {'Lower': np.array([160, 0, 50]), 'Upper': np.array([180, 255, 255])},
              }

cap = cv2.VideoCapture(0)
cv2.namedWindow('camera', cv2.WINDOW_AUTOSIZE)

while (1):
    ret, frame = cap.read()

    gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
    kernel = np.ones((3, 3), np.uint8)
    erode_hsv = cv2.erode(hsv,kernel, iterations=1)                   # 腐蚀 粗的变细
    erode_hsv = cv2.erode(hsv,kernel, iterations=1)                   # 腐蚀 粗的变细
    
    
    
    inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    count=0
    ##detect red####################################
    inRange_hsv = cv2.inRange(erode_hsv, color_dist['red']['Lower'], color_dist['red']['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    for pic, contour in enumerate(cnts):
        count=count+1

    for pic, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if(area > 1000 ):
        #box = cv.minAreaRect(contour)
        #box = np.int0(cv.boxPoints(box)) 
        #cv.drawContours(originImg, [box], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour) 
            
            e = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) 
			
            cv2.putText(frame, "red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255)) 
    ###############################################     
    ##detect green#################################
    inRange_hsv = cv2.inRange(erode_hsv, color_dist['green']['Lower'], color_dist['green']['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
   
    for pic, contour in enumerate(cnts):
        count=count+1

    for pic, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if(area > 1000 ):
        #box = cv.minAreaRect(contour)
        #box = np.int0(cv.boxPoints(box)) 
        #cv.drawContours(originImg, [box], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour) 
            
            e = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
			
            cv2.putText(frame, "green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0)) 
    ##############################################
    ##detect blue#################################
    inRange_hsv = cv2.inRange(erode_hsv, color_dist['blue']['Lower'], color_dist['blue']['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
   
    for pic, contour in enumerate(cnts):
        count=count+1

    for pic, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if(area > 1000 ):
        #box = cv.minAreaRect(contour)
        #box = np.int0(cv.boxPoints(box)) 
        #cv.drawContours(originImg, [box], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour) 
            
            e = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
			
            cv2.putText(frame, "blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0)) 
    ###############################################
    ##detect pink##################################
    inRange_hsv = cv2.inRange(erode_hsv, color_dist['pink']['Lower'], color_dist['pink']['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
           
    
    for pic, contour in enumerate(cnts):
        count=count+1

    for pic, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if(area > 1000 ):
        #box = cv.minAreaRect(contour)
        #box = np.int0(cv.boxPoints(box)) 
        #cv.drawContours(originImg, [box], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour) 
            
            e = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 13, 266), 2) 
			
            cv2.putText(frame, "pink", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 13, 266))
    #############################################
    ##detect yellow##############################
    inRange_hsv = cv2.inRange(erode_hsv, color_dist['yellow']['Lower'], color_dist['yellow']['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
   
    for pic, contour in enumerate(cnts):
        count=count+1
            
    for pic, contour in enumerate(cnts):
        area = cv2.contourArea(contour)
        if(area > 1000 ):
        #box = cv.minAreaRect(contour)
        #box = np.int0(cv.boxPoints(box)) 
        #cv.drawContours(originImg, [box], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour) 
            
            e = cv2.rectangle(frame, (x, y), (x + w, y + h), (12, 237, 245), 2) 
			
            cv2.putText(frame, "yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (12, 237, 245))
    ############################################

    cv2.imshow('camera', frame)
    cv2.waitKey(1)


cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
