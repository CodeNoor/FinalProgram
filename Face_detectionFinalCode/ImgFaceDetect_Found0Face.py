import cv2
import sys

imagePath = ("image\image4.jpg")

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)
print("...\n\t")
print("Found {0} Faces!\n\t".format(len(faces)))

for (x, y, w, h) in faces:
    # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    padding = 300
    cv2.rectangle(image,(x-padding,y-padding),(x+w+padding,y+h+padding),(255,0,0),cv2.FILLED)
# cv2.imshow('Detected Faces in Image',image)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
status = cv2.imwrite('faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

