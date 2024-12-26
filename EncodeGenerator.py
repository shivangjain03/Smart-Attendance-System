import cv2
import face_recognition
import pickle
import os

folderModePath = "Resources/Modes"
modePath = os.listdir(folderModePath)
imgModeList = []
for imgPath in modePath:
    img = cv2.imread(os.path.join(folderModePath, imgPath))
    imgModeList.append(img)

