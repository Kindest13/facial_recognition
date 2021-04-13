import face_recognition
from pathlib import Path
from PIL import Image, ImageDraw

def markUnknownFaces(image_to_mark, analytics):
    image_of_team = face_recognition.load_image_file('./team/team.jpg')
    known_face_encodings = face_recognition.face_encodings(image_of_team)
    known_faces_presence = [False] * len(analytics)
    unknown_face_is_present = False

    # Find faces in test image
    face_locations = face_recognition.face_locations(image_to_mark)
    face_encodings = face_recognition.face_encodings(image_to_mark, face_locations);

    # Convert to PIL format 
    pil_image = Image.fromarray(image_to_mark)

    # Create a ImageDraw instance

    draw = ImageDraw.Draw(pil_image)

    # Loop through faces in test image
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.55)
        
        for index, match in enumerate(matches):
            # Pass already recognized faces
            if known_faces_presence[index]:
                continue
            analytics[index] = analytics[index] + match
            known_faces_presence[index] = match
        # If not match Draw Box
        if not any(matches):
            draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0), width=5)
            unknown_face_is_present = True

    del draw

    if unknown_face_is_present:
        return pil_image
    
    return None
