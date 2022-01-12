import cv2
image = cv2.imread('image/image1.jfif')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(image,1.3,5)
for (x,y,w,h) in faces:
    #Enclose the detected faces inside a rectangular filling the total face
    # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),cv2.FILLED)
    padding = 20
    cv2.rectangle(image,(x-padding,y-padding),(x+w+padding,y+h+padding),(255,0,0),cv2.FILLED)

cv2.imshow('Detected Faces in Image',image)
cv2.waitKey(5000)
cv2.destroyAllWindows()