from deepface import DeepFace
import os
import cv2

img1_path = 'image/ping_1.png'
img2_path = 'image/Oak_3.png'

img_1 = cv2.imread(img1_path)
img_2 = cv2.imread(img2_path)

result = DeepFace.verify(img1_path, img2_path, model_name = 'ArcFace')
print(result)