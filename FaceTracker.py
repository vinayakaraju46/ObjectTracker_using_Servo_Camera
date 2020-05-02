import cv2
import numpy as np
import pigpio

pi = pigpio.pi()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 320)

_, frame = cap.read()
rows, cols, _ = frame.shape

x_medium = int(cols / 2)
center = int(cols / 2)
position = 1500 # degrees
pi.set_servo_pulsewidth(17, position)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        x_medium = int((x + x + w) / 2)
        break

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break

    # Move servo motor
    if x_medium < center -30:
        position += 20
    elif x_medium > center + 30:
        position -= 20
	
    if position > 2500:
	position -= 20
    if position < 500:
	position += 20
    pi.set_servo_pulsewidth(17, position) 

    #pwm.setServoPosition(0, position)
    
cap.release()
cv2.destroyAllWindows()





    
