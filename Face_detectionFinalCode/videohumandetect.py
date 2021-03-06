# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 11:47:27 2019

@author: vchan
"""

# OpenCV Python program to detect pedestrians in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
cap = cv2.VideoCapture('video1.mp4',0)

# Trained XML classifiers describes some features of some object we want to detect
pedestrian_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    #gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    # Detects pedestrians of different sizes in the input image
    pedestrians = pedestrian_cascade.detectMultiScale( frames, 1.1, 1)
    # To draw a rectangle in each pedestrians
    for (x,y,w,h) in pedestrians:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,0),2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frames, 'Person', (x + 6, y - 6), font, 0.5, (0, 255, 0), 500)
        # Display frames in a window
        cv2.imshow('Pedestrian detection', frames)
    # Wait for Enter key to stop
    if cv2.waitKey(33) == 13:
        break

cap.release()
cv2.destroyAllWindows()