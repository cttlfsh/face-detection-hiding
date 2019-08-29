import cv2
import argparse
import numpy as np

# filename = "/home/cttlfsh/Desktop/square_faces.jpg"

class FaceDetection():
  '''
  Class which handles the face detection and hiding. It loads an image and by default
  detects faces in it via a CascadeClassifier algorithm (Viola-Jones Face Detection
  Algorithm). Optionally contains methods for hiding the detected faces through 
  different methods, such as blur, pixel shuffling, negative and image swapping.
  
  @param filename: the path of the image to load
  '''
  def __init__(self, filename):
    self.swap_image = "/home/cttlfsh/Desktop/grrr_reaction.png"
    self.methods = ['blur', 'shuffle', 'negative', 'image_swap']
    # Loading image
    self.img_raw = cv2.imread(filename)
    # Create and load the CascadeClassifier for face detection
    self.haar_cascade_face = cv2.CascadeClassifier()
    if not self.haar_cascade_face.load('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'):
      raise FileNotFoundError
    
    [self.detected_faces, self.final_image] = self.detect_face(self.img_raw)
    
    
  
  def detect_face(self, image):
    '''
    Method to detect faces in an image. It uses OpenCV for converting into grey scale
    the image and than applying on it the `detectMultiScale` function, which detects the faces.
    Noteworthy are the paramenters of this function, `scaleFactor` and `minNeighbors`. The 
    former deals with the distance that the detected faces have from the camera and the latter
    with the amount of neighbors (see Viola-Jone for more detail) a rectangle must have in 
    order to be considered a face.
    At last, once the face(s) is recognized, the rectangle(s) is drawn into the image.
    
    @param image: the image onto which detect faces
    @return [rect, img]: a tuple containing both the processed images (with rectangles already drawn)
                         and the details of the rectangles themselves
    '''
    # Converting image to grey-scale
    self.img_raw_grey = cv2.cvtColor(self.img_raw, cv2.COLOR_BGR2GRAY)
    # Detecting faces
    self.faces_rects = self.haar_cascade_face.detectMultiScale(self.img_raw_grey, scaleFactor = 1.2, minNeighbors = 3);
    # print('Faces found: ', len(self.faces_rects))
    # Drawing rectangles on the image
    for (x,y,w,h) in self.faces_rects:
      rect = {
        'x': x,
        'y': y,
        'w': w,
        'h': h
      }
      img = cv2.rectangle(self.img_raw, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return [rect, img]
      
      
  
  def hide_face(self, hide_method):
    '''
    Methods which hides the faces in a image with the preferred method. The supported
    methods can be accessed with the property `methods`. As far as `image_swap` is concerned,
    at the moment is not possible to change the image which replaces the face.
    
    @param hide_method: the hiding method
    @return final_image: the image after the hiding process 
    '''
    y = self.detected_faces['y']
    x = self.detected_faces['x']
    w = self.detected_faces['w']
    h = self.detected_faces['h']
    if not hide_method in self.methods:
      raise KeyError
    elif hide_method == 'blur':
      self.final_image[y:y+h, x:x+w] = cv2.blur(self.final_image[y:y+h, x:x+w], (40, 40))
    elif hide_method == 'shuffle':
      np.random.shuffle(self.final_image[y:y+h, x:x+w].flat)
    elif hide_method == 'negative':
      self.final_image[y:y+h, x:x+w] = cv2.bitwise_not(self.final_image[y:y+h, x:x+w])
    elif hide_method == 'image_swap':
      self.swap_image_raw = cv2.imread(self.swap_image)    
      self.swap_image_resize = cv2.resize(self.swap_image_raw, (w, h)) 
      self.final_image[y:y+h, x:x+w] = self.swap_image_resize
    return self.final_image
      
      
  
def main():
  parser = argparse.ArgumentParser(description="Parameter handler for face recognition script")
  parser.add_argument("--filename", "-f", type=str, required=True, help="Path to an image file")
  parser.add_argument("-p", "--privacy", type=bool, default=False, required=False, help="Enable face hiding for privacy issue")
  parser.add_argument("-m", "--hide_method", type=str, default='blur', required=False, help="Method for hiding faces, choose among: blur, shuffle, negative, image_swap")
  arguments = parser.parse_args()
  try:
    f = FaceDetection(arguments.filename)
    img = f.final_image
    if arguments.privacy:
      try:
        img = f.hide_face(arguments.hide_method)
      except KeyError:
        print('Hide method not supported')
    cv2.imshow('Processed Image', img)
    cv2.waitKey(0) 
  except FileNotFoundError:
    print("Pre-training for Cascade Classifier not found")
    
  
    


if __name__ == '__main__':
  main()
  
