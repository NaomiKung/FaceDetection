import cv2
import face_recognition
import dlib
from Model.facenet_basemodel import FaceNet
from process.resize import resize
from process.crop_face import video_face
path = './image/'


cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FaceNet().loadModel('./Model/facenet_weights.h5')

while True:
    ret, frame = cap.read()
    ret2 , frame2 = cap.read()

    if ret and ret2 == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.1, 4)

        face_crop = video_face(faces, frame, frame2)

        face_re = resize(face_crop)

        try:
            result = model.predict(face_re)
            print(result.shape)
        except:
            print("result can't find")

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

cap.release()
cv2.destroyWindow()