# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:09:19 2021

@author: natha
"""

import cv2

cap = cv2.VideoCapture(0)

# face_cascade = cv2.CascadeClassifier('./imported_model/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('./imported_model/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('./imported_model/haarcascade_lefteye_2splits.xml')

while True:
    ret, img = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.08, 5)    
    
    for x, y, w, h in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
        
    cv2.imshow('Output', img)
    if cv2.waitKey(10) > 0 :
        break
cap.release()
cv2.destroyAllWindows()
        