import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from model import readStudent

#c is student class
def Attend(c, s):
    cl = c
    path = 'Images'
    images = [] #store images
    clasNames = [] #store images name with no .jpg
    myList = readStudent(cl) #stores list of images in the path 'Images'

    if myList != "":
        print(myList)
        for cls in myList:
            curimg = cv2.imread(f'{path}/{cl}/{cls}')
            images.append(curimg)
            clasNames.append(os.path.splitext(cls)[0]) #split paths first part befre jpg and stores in the list

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert images from bgr to rgb
                encode = face_recognition.face_encodings(img)[0]#encode each img
                encodeList.append(encode) #append encoding of each img to the list
            return encodeList

        def markAttendance(name):
            with open('attendance.csv', "r+") as f:
                myDataList = f.readlines()
                nameList = [] #stores name list
                # print(myDataList)
                for line in myDataList:
                    entry = line.split(',')
                    if entry[2] != 'Name':
                        nameList.append(entry[2])
                if name not in nameList:
                    now = datetime.now()
                    # print(now)
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{c},{s},{name},{dtString}')

        encodeListKnown = findEncodings(images)
        # print(len(encodeListKnown))
        print("Encoding complete!")

        cap = cv2.VideoCapture(0) #capture video

        while True:
            success, img = cap.read()
            imgs = cv2.resize(img,(0,0), None, 0.25,0.25) #create small image by resizing
            imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

            facesCurrFrame = face_recognition.face_locations(imgs)
            encodeCurrFrame = face_recognition.face_encodings(imgs, facesCurrFrame)

            for encodeFace,faceLoc in zip(encodeCurrFrame,facesCurrFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace) #comparing stored known encodings of images with the captured image face encode
                facDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(facDis)
                matchIndex = np.argmin(facDis) #index of min value arg

                if matches[matchIndex]: #if match is true of the min val index
                    name = clasNames[matchIndex].upper() #stores match classname
                    y1, x2, y2, x1 = faceLoc #storing 4 locs
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 #need to resize locations since it was resized to small img
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2) #outline rectangle around face
                    cv2.rectangle(img, (x1, y2-35), (x2, y2), (255, 0, 255), cv2.FILLED) #filled rectangle
                    cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2) #put text on fileed rectangle
                    markAttendance(name)


            cv2.imshow('webcam',img)
            k = cv2.waitKey(1)
            if k % 256 == 32: #Space Key for close webcam
                cap.release()
                cv2.destroyAllWindows()
                break
        return True
    else:
        return False