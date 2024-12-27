import cv2
import face_recognition
#import face_recognition
import pickle
import os

folderPath = "Images"
Path = os.listdir(folderPath)

imgList = []
studentId=[]
for imgPath in Path:
    img = cv2.imread(os.path.join(folderPath, imgPath))
    imgList.append(img)
    studentId.append(os.path.splitext(imgPath)[0])
print(studentId)


def FindEncodings(imgList):
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
