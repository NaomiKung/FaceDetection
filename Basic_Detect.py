import face_recognition
import cv2
import numpy as np

imgOak = face_recognition.load_image_file('image/Oak_1.png')
imgOak = cv2.cvtColor(imgOak, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('image/Krit_1.png')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgOak)[0]
encodeOak = face_recognition.face_encodings(imgOak)[0]
cv2.rectangle(imgOak, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),(255,0,255))

faceLoc = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),(255,0,255))

results = face_recognition.compare_faces([encodeOak], encodeTest)
faceDis = face_recognition.face_distance([encodeOak], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_ITALIC, 1, (255,0,255), 2)

cv2.imshow('Oak', imgOak)
cv2.imshow('Test', imgTest)
cv2.waitKey(0)