from Model.facenet_basemodel import FaceNet
import os
import cv2
from annoy import AnnoyIndex

path = './image/Oak.png'
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(gray, 1.1, 4)
for x, y, w, h in faces:
    img_crop = img[x:x+w, y:y+h]

img_re = cv2.resize(img_crop,(160,160))
img_re = img_re[None,:,:,:]

model = FaceNet().loadModel('./Model/facenet_weights.h5')
ans = model.predict(img_re).reshape(-1, 1)

t= AnnoyIndex(128, 'euclidean')
t.load('result.ann')

idx = t.get_nns_by_vector(ans, 1)

print(t[6][0])
