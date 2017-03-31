import cv2
import os
import sys
from string import Template
from PIL import Image

# first argument is the haarcascades path
face_cascade_path = sys.argv[1]
face_cascade = cv2.CascadeClassifier(os.path.expanduser(face_cascade_path))

scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)
flags = cv2.cv.CV_HAAR_SCALE_IMAGE

count = 1

for infname in sys.argv[2:]:
   image_path = os.path.expanduser(infname)
   image = cv2.imread(image_path)

   faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor, minNeighbors = min_neighbors,
    minSize = min_size, flags = flags)

   for( x, y, w, h ) in faces:
     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
     outfname = "%s.faces.jpg" % os.path.basename(infname)
     cv2.imwrite(os.path.expanduser(outfname), image)

     img = Image.open(image_path)
     x = img.crop ((x, y, x+w, y+h))
     x.save ('subject' + str (count) + '.jpg')
     #img.close()
     count += 1