import numpy as np
import cv2

filename = "images/square_faces.jpg"
grrr = "images/grrr_reaction.png"

# Loading image
img_raw = cv2.imread(filename)
grrr_image = cv2.imread(grrr)
# print(img_raw[1:10,1:10])

# Converting image to grey-scale
img_raw_grey = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
# Create and load the CascadeClassifier for face detection
haar_cascade_face = cv2.CascadeClassifier()
loaded = haar_cascade_face.load('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

'''
Returns a rectangle around the face.

@param scale_factor: compensate the distance of the face from the camera
@param minNeighbors: number of neighbors for a rectangle to be considered as a face
'''
faces_rects = haar_cascade_face.detectMultiScale(img_raw_grey, scaleFactor = 1.2, minNeighbors = 3);
print('Faces found: ', len(faces_rects))
for (x,y,w,h) in faces_rects:
  # print(x, y, w,h)
  cv2.rectangle(img_raw, (x, y), (x+w, y+h), (0, 255, 0), 2)
  # UNCOMMENT THE DESIRED HIDING METHOD
  # 1] BLUR
  # img_raw[y:y+h, x:x+w] = cv2.blur(img_raw[y:y+h, x:x+w], (40, 40))
  # 2] SHUFFLING PIXELS
  # np.random.shuffle(img_raw[y:y+h, x:x+w].flat)
  # 3] NEGATIVE
  # img_raw[y:y+h, x:x+w] = cv2.bitwise_not(img_raw[y:y+h, x:x+w])
  # 4] EMOJI
  # grrr_resize = cv2.resize(grrr_image, (w, h)) 
  # img_raw[y:y+h, x:x+w] = grrr_resize
  

fromCenter = False
roi = cv2.selectROI("", img_raw, fromCenter)
img_raw[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]] = cv2.blur(img_raw[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]], (40, 40))

cv2.imwrite('results/simple_output.png', img_raw)
cv2.imshow('img', img_raw)
cv2.waitKey(0) 