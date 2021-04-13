import cv2
import sys
import os
import face_recognition
from PIL import Image, ImageDraw

from utils_faces.get_faces import getFaces
sys.path.append('..')
from utils.create_folder import createFolder

def saveFaces(team_image):
    # faces = getFaces(team_image)
    faces = face_recognition.face_locations(team_image)
    team_path = createFolder('./team', 'faces', True)
    face_id = 1
        
    for (top, right, bottom, left) in faces:
        face = team_image[top:bottom, left:right]
        team_faces_path = os.path.join(team_path, f'{face_id}.jpg')
        pil_image = Image.fromarray(face)
        pil_image.save(team_faces_path)
        face_id += 1
