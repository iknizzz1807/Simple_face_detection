import cv2
# OpenCV library in python is blessed with many pre-trained classifiers for face, eyes, smile, etc.

face_cascade = cv2.CascadeClassifier('model.xml')
# Load the model

img = cv2.imread('input_images/face.jpg')
# Make an image a variable

faces = face_cascade.detectMultiScale(img, 1.1, 4)
# This is the code that detects faces in an image

for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("output_images/face_detected.png", img)
print('Successfully saved')
# Draw rectangles around the detected faces and save new image


