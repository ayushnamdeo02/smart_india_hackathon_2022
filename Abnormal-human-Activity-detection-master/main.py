import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

Sec = 0
Min = 0
Check = 1
Counter = 1

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)     

    if len(faces) > 0:  

        Sec += 1
        print(str(Min) + " Mins " + str(Sec) + " Sec ")

        cv2.putText(img, "Time: " + str(Min) + " Mins " + str(Sec) + " Sec ", (0,img.shape[0] -30), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)
        cv2.putText(img, "Number of faces detected: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)    

        time.sleep(1)
        if Sec == 60:
            Sec = 0
            Min += 1
            print(str(Min) + " Minute")

                   
    if len(faces) == 0:

        print('No face detected')
        cv2.putText(img, "No face detected ", (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)        
        Sec = 0
        Min = 0

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break    

cap.release()
cv2.destroyAllWindows()
