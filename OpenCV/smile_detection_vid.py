import numpy as np
import cv2

#load some pre_trained data on face frontals from opencv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('OpenCV/haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('OpenCV/haarcascade_smile.xml')
#capture video from webcam
webcam = cv2.VideoCapture(0)

while True:
  #read the current frame
  successful_frame_read, frame = webcam.read()
  #if there's an error, abort
  if not successful_frame_read:
    break
  #must convert to grayscale
  grayscaled_webcam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #detect faces
  face_coordinates = trained_face_data.detectMultiScale(grayscaled_webcam)
  
  #draw rectangles
  for (x, y, w, h) in face_coordinates:
    #get the sub-frame which contains only the faces
    the_face = frame[y:y+h ,x:x+w]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
    smile_coordinates = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)
    #find all smiles in the face
    #for (x_, y_, w_, h_) in smile_coordinates:
     # cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (50, 50, 200), 2)
    
    if len(smile_coordinates) > 0:
      cv2.putText(frame, 'Dog', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, color=(0, 0, 255))
    else:
      cv2.putText(frame, 'Human', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, color=(255, 0, 0))
  cv2.imshow('Dog/Human Detector', frame)
  key = cv2.waitKey(1)
  #press q to stop
  if key==81 or key==113:
    break

webcam.release()