import cv2

def video_face(faces,frame,frame2):
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face_1', (x + 6, y - 6), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
        face_crop = frame2[x:x + w, y:y + h]

        return face_crop

def img_face(images):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(images)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 4)
    try :
        x, y, w, h = faces
    except :
        print(img + "Face can't find")
    face_crop = images[x:x + w, y:y + h]

    return face_crop