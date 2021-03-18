import cv2
import face_recognition
import dlib
from Model.facenet_basemodel import FaceNet
from preprocess_image.resize import resize
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

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Face_1', (x + 6, y - 6), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
            face_crop = frame2[x:x + w, y:y + h]

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