import numpy as np
import cv2

#load some pre_trained data on face frontals from opencv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('mindvu/Documents/Code/python/OpenCV/haarcascade_frontalface_default.xml')

#choose an image to detect faces in
img = cv2.imread('mindvu/Documents/Code/python/OpenCV/test.jpg')

#must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#face detection
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangle
for i in face_coordinates:
  (x, y, w, h) = i
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#print(face_coordinates)
#
cv2.imshow('Face Detector', img)
cv2.waitKey()