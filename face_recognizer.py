#!/usr/bin/python

# Import the required modules
import cv2, os
import numpy as np
from PIL import Image

def doFaceRecognition():
# For face detection we will use the Haar Cascade provided by OpenCV.
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    # For face recognition we will the the LBPH Face Recognizer 
    recognizer = cv2.createLBPHFaceRecognizer()

    path = './crop'

    present_student = [] #list to hold the sap ids of present students. I guess it is stored in variable
    recognizer.load("model.yml")

    # Append the images with the extension .jpg into image_paths
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    for image_path in image_paths:
        predict_image_pil = Image.open(image_path).convert('L')
        predict_image = np.array(predict_image_pil, 'uint8')
        faces = faceCascade.detectMultiScale(predict_image)
        for (x, y, w, h) in faces:
            nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
            nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
            if nbr_actual == nbr_predicted:
                print "{} is first wala recognized as {}".format(nbr_actual, conf)
            else:
                #print "{} is second wala recognized as {}".format(nbr_actual, nbr_predicted)
                present_student.append(nbr_predicted)

            #cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
            #cv2.waitKey(1000)
    for studens in present_student:
        print studens
    return present_student