import numpy as np
import cv2

#load some pre_trained data on face frontals from opencv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('OpenCV\haarcascade_frontalface_default.xml')

#capture video from webcam
webcam = cv2.VideoCapture(0)

while True:
  #read the current frame
  successful_frame_read, frame = webcam.read()
  #must convert to grayscale
  grayscaled_webcam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #detect faces
  face_coordinates = trained_face_data.detectMultiScale(grayscaled_webcam)
  #draw rectangles
  for (x, y, w, h) in face_coordinates:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
  #
  cv2.imshow('Face Detector', frame)
  key = cv2.waitKey(1)
  #press q to stop
  if key==81 or key==113:
    break

webcam.release()