import cv2, os, numpy as np

cap = cv2.VideoCapture(0)
path = './image/'
p = e = 0
nameList = []

while True:
    _, frame = cap.read()

    key = cv2.waitKey(1)
    if key == ord('n'):
        name = input()
        nameList.append(name)

    if key == ord('p'):
        p +=1
        cv2.imwrite(path + name + '_' + str(p) + '.jpg' , frame)

    if key == ord('q'):
        break

    cv2.imshow('frame', frame)
