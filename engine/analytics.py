import face_recognition
from pathlib import Path
import shutil, os
import cv2
from PIL import Image, ImageDraw

from mark_unknown import markUnknownFaces
from mark_presence import markPresenceAnalysis
from utils.create_folder import createFolder




def moveSnapshots():
    root = Path(".")
    origin_dir = root / "analytics"
    snapshots_dir = root / "snapshots"
    dest_dir = createFolder(origin_dir, '1', False)

    files = [f.name for f in os.scandir(snapshots_dir) if f.is_file()]

    for file in files:
        file_path = os.path.join(snapshots_dir, file)
        shutil.move(file_path, dest_dir)

    return dest_dir



    
def analytics():
    origin_dir = moveSnapshots()

    image_of_team = face_recognition.load_image_file('./team/team.jpg')

    team_face_locations = face_recognition.face_locations(image_of_team)
    team_face_encodings = face_recognition.face_encodings(image_of_team)
    face_analytics = [0] * len(team_face_encodings)

    files = [f.name for f in os.scandir(origin_dir) if f.is_file()]

    for file in files:
        # Read the image
        file_path = os.path.join(origin_dir, file)
        unknown_image = face_recognition.load_image_file(file_path)

        markedImage = markUnknownFaces(unknown_image, face_analytics)
        if markedImage:
            path_to_save = os.path.join('./email', file)
            markedImage.save(path_to_save)
        

    markPresenceAnalysis(face_analytics, len(files))
        