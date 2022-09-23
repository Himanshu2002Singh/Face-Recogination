import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
# from PIL import ImageGrab
 # make a list of image for taken multiple images 
path = 'imageBasic'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
curImg = cv2.imread(f'{path}/{cl}')
images.append(curImg)
classNames.append(os.path.splitext(cl)[0])
print(classNames)

  # encoding of each eimage that means convert each image BGR TO RGB formate

def findEncodings(images):
encodeList =[]
for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
   return encodeList

# mark the attendence of matching image and update the attendence list...

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
     myDataList = f.readlines()
     nameList = []
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
    if name not in nameList:
           now = datetime.now()
           dtString = now.strftime('%H:%M:%S')
           f.writelines(f'\n{name},{dtString}')
 
#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
 
encodeListKnown = findEncodings(images)
print('Encoding Complete')
 

 # take a image from webcam using module cv2.VideoCapture and then encoding of converting BGR to RGB

cap = cv2.VideoCapture(0)
 
while True:
     success, img = cap.read()
      #   img = captureScreen() & resize ....
      imgS = cv2.resize(img,(0,0),None,0.25,0.25)
      #  img covert BGRto RGB .......
      imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  
       # second step.......
     facesCurFrame = face_recognition.face_locations(imgS)
     encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
     # third step compare_faces......
     for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

  # check index which are contain less value (arround 0.5)  then find this index and print name with CAppital latter....

        if matches[matchIndex]:
           name = classNames[matchIndex].upper()
            #print(name)
   # make a bounding box of matching image.........

          y1,x2,y2,x1 = faceLoc
          y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
          cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
          cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
          cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
markAttendance(name)
 
cv2.imshow('Webcam',img)
cv2.waitKey(1)