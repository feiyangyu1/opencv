import cv2
import numpy as np
import random

# read, resize and show the image
img = cv2.imread('babyYoda.jpeg')

img = cv2.resize(img, (400, 300))
cv2.imshow('img', img)
cv2.waitKey(0)


# read, resize, and play the video. press Q to quit the play
cap = cv2.VideoCapture('dog.mp4')

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break

# check the shape and the type of this image variable
img = cv2.imread('babyYoda.jpeg')
print(img.shape)
print(type(img))

# create an image with random color
img = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        img[row][col] = [random.randint(0, 255),
        random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('img', img)
cv2.waitKey(0)

# show a part of the image
img = cv2.imread('babyYoda.jpeg')
newImg = img[:150, 100:400]
cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)

# modify the image
img = cv2.imread('babyYoda.jpeg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (9, 9), 5)
canny = cv2.Canny(img, 150, 200)

kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(canny, kernel, iterations=1)

kernel1 = np.ones((3, 3), np.uint8)
erode = cv2.erode(dilate, kernel1, iterations=2)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)
