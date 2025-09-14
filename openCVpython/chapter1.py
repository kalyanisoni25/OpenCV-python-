import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

mycolors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]
mycolorvalues = [[199,11,175],
                 [0,12,179],
                 [77,255,75]]
mypoints = []

def findcolor(img,mycolors,mycolorvalues):
    count = 0
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in mycolors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getcontours(mask)
        cv2.circle(imgResult,(x,y),10,mycolorvalues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(color[0]), mask)
    return newPoints

def getcontours(img):
    x,y,w,h = 0,0,0,0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(  imgResult  , cnt , -1 , (255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            x,y,w,h = cv2.boundingRect(cnt)

    return x+w//2, y

def drawOncanvas(mypoints,mycolorvalues):
    for point in mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, mycolorvalues[point[2]], cv2.FILLED)



while(True):

    success, img = cap.read()

    imgResult = img.copy()
    newPoints = findcolor(img, mycolors,mycolorvalues)

    if len(newPoints)!=0:

         for newP in newPoints:
                mypoints.append(newP)
    if len(mypoints)!=0:
        drawOncanvas(mypoints,mycolorvalues)
    cv2.imshow("result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break