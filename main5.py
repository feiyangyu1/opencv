import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def findBall(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(len([0,179,120,189,50,209])):
        lower = np.array([0,120,50])
        upper = np.array([179,189,209])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        ballx, bally = findContour(mask)
        cv2.circle(imgContour, (ballx, bally), 10, (255,0,0), cv2.FILLED)
        if bally != -1:
            drawPoints.append([ballx, bally, i])
    #findContour(mask)
    #cv2.imshow('result', result)

def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1,-1,-1,-1
    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)
    return x+w//2, y+h//2

drawPoints = []

def draw(drawPoints):
    for point in  drawPoints:
        cv2.circle(imgContour,(point[0], point[1]), 10,[0,165,255],cv2.FILLED)

while True:
    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('video', frame)
        findBall(frame)
        draw(drawPoints)
        cv2.imshow('contour', imgContour)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break

