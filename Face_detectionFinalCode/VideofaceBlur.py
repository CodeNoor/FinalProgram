'''
Simple Face Blur on a live webcam video streams using Gausian Blur
'''

import cv2
video_cam = cv2.VideoCapture('video1.mp4')
# Haar Cascade to detect frontal faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret, image_frame = video_cam.read()
    # Detect faces in the Webcam Video Stream
    faces = face_cascade.detectMultiScale(image_frame,1.3,5)
    for (x,y,w,h) in faces:
        # Enclose inside a blue rectangular box
        #  padding = 10
        #  cv2.rectangle(image_frame,(x-padding,y-padding),(x+w+padding,y+h+padding),(255,0,0),3)
        cv2.rectangle(image_frame,(x,y),(x+w,y+h),(255,0,0),300)
        # Select only detected face portion for Blur
        face_color = image_frame[y:y + h, x:x + w]
        # Blur the Face with Gaussian Blur of Kernel Size 51*51
        blur = cv2.GaussianBlur(face_color, (51, 51), 0)
        image_frame[y:y + h, x:x + w] = blur
    # Display the Blurred Faces
    cv2.imshow('Detected Face',image_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_cam.release()
cv2.destroyAllWindows()