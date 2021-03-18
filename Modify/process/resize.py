import cv2

def resize(face_crop):
    shape_crop = face_crop.shape
    if shape_crop[0] >= 160:
        try:
            face_re = cv2.resize(face_crop, dsize=(160, 160), interpolation=cv2.INTER_CUBIC)
        except:
            print("Less resize Error")
    else:
        try:
            face_re = cv2.resize(face_crop, dsize=(160, 160), interpolation=cv2.INTER_CUBIC)
        except:
            print('Than resize Error')

    face_re = face_re[None,:,:,:]
    return face_re