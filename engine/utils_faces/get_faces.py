import cv2
import sys
from PIL import Image, ImageDraw

def getFaces(image_with_faces):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

    # Read the image
    gray = cv2.cvtColor(image_with_faces, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        1.05,
        4
    )

    print("Found {0} faces!".format(len(faces)))

    return faces
