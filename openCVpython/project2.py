import cv2
import numpy as np

from chapter1 import imgResult

widthImg = 640
heightImg = 480


cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imageCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imageCanny, None, iterations=2)
    imgThres = cv2.erode(imgDial,kernel, iterations = 1)

    return imgThres

def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContour(imgContor,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,0.02*per,True)
            print(len(approx))
            objcor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgCount = img,copy()
    imgThres = preProcessing(imgThres)
    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break