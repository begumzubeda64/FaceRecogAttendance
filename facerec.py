import cv2
import numpy as np
import face_recognition

img = face_recognition.load_image_file("Images/elon real.jpg") #load image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting default format bgr to rgb

img_test = face_recognition.load_image_file("Images/Elon Musk.jpg") #load image
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB) #converting default format bgr to rgb

faceloc = face_recognition.face_locations(img)[0] #location of first image as top, right, bottom, left pos
encodeElon = face_recognition.face_encodings(img)[0]
cv2.rectangle(img, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)
#image, left,right, top,bottom, color of rectangle, thickness

facelocTest = face_recognition.face_locations(img_test)[0] #location of first image as top, right, bottom, left pos
encodeTest = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_test, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(img_test, f"{results} {round(faceDis[0], 2)}", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

cv2.imshow('Elon Musk',img) #show text on img
cv2.imshow('Elon Test',img_test)
cv2.waitKey(0)
