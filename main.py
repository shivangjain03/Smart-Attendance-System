import cv2
import os
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("Resources/background.png")
folderModePath = "Resources/Modes"
modePath = os.listdir(folderModePath)
imgModeList = []
for imgPath in modePath:
    img = cv2.imread(os.path.join(folderModePath, imgPath))
    imgModeList.append(img)

while True:
    success, img = cap.read()
    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[1] 
    cv2.imshow("Webcam Check", img)
    cv2.imshow("Face Attendace System", imgBackground)
    cv2.waitKey(1)
    


