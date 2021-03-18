import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime

path = 'image'
images = []
classNames = []
p_name = []
myList = os.listdir(path)

while True:
    type_log = int(input("1 : Log in \n2 : Log out\nChoose :"))
    if type_log == 1:
        type_log = "Log in"
        print("Log in system.")
        break
    elif type_log == 2:
        type_log = "Log out"
        print("Log out system.")
        break
    else:
        print("Error input please fill again.")
        
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    if '.png' in cl:
        classNames.append(cl.split('_')[0])

for i in classNames:
    if i not in p_name:
        p_name.append(i)
print(p_name)

def findEncoding(images):
    encodeList = []
    error_encode = []
    i=0
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
        except:
            error_encode.append(classNames[i])
        encodeList.append(encode)
        i+=1
    return encodeList
    print("Error encode is ",error_encode)

def create_csv(files, path, table_in, table_out):
    if table_in and table_out not in files:
        open(f'{path}{table_in}', 'x')
        open(f'{path}{table_out}', 'x')
        with open(f'{path}{table_in}', 'r+') as f:
            f.writelines("Name, Date, Time, Type")
        with open(f'{path}{table_out}', 'r+') as f:
            f.writelines("Name, Date, Time, Type")


def markAttendance(name, path, table_in, table_out, type_log):
    with open(f'{path}{table_in}','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if (name not in nameList) and type_log == "Log in":
            now = datetime.now()
            dtString = now.strftime('%d:%m:%Y,%H:%M:%S')
            f.writelines(f'\n{name}, {dtString},{type_log}')
    with open(f'{path}{table_out}', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if (name not in nameList) and type_log == "Log out":
            now = datetime.now()
            dtString = now.strftime('%d:%m:%Y,%H:%M:%S')
            f.writelines(f'\n{name}, {dtString},{type_log}')

encodeListKnown = findEncoding(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    x = datetime.now()
    path = './service/attendance/Daily/'
    table_in = "attendance" + '_' + x.strftime('%d%m%Y') + "_login.csv"
    table_out = "attendance" + '_' + x.strftime('%d%m%Y') + "_logout.csv"
    files = os.listdir(path)
    create_csv(files, path, table_in, table_out)

    # img = captureScreen()
    if ret:
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS, model='hog')
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
        faceDis_1 = np.array(faceDis)[0]
        faceDis_1 = round(faceDis_1, 2)

        '''
               ระบุบตำแหน่งใบหน้าและ Track face with rectangle
        '''
        if faceDis_1 >= 0.6:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

            if matches[matchIndex] :
                name = classNames[matchIndex].upper()
            #print(name)
                cv2.rectangle(img,(x1,y1),(x2,y2), (255,0,255), 2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2+25),(255,0,255), cv2.FILLED)

                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
                cv2.putText(img, str(faceDis_1), (x1, y2+25), cv2.FONT_ITALIC, 1, (0,0,0), 2)
               
                markAttendance(name, path, table_in, table_out, type_log)
        elif faceDis_1 < 0.6:
            cv2.rectangle(img,(x1,y1),(x2,y2), (255,0,255), 2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2+25),(255,0,255), cv2.FILLED)
            cv2.putText(img, "UnKnow", (x1 + 6, y2 - 6), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
        else:
            print("Error FaceDis")

    cv2.putText(img, type_log, (0,40), cv2.FONT_ITALIC, 2, (0,0,0), 4)
    cv2.imshow('Webcam', img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

    if key == ord('1'):
        type_log = "Log in"

    if key == ord("2"):
        type_log = "Log out"
    
cap.release()
cv2.destroyWindow("Webcam")