import face_recognition
from pathlib import Path
from PIL import Image, ImageDraw

def markUnknownFaces(image_to_mark, analytics):
    imageOfTeam = face_recognition.load_image_file('./team/team.jpg')
    knownFaceEncodings = face_recognition.face_encodings(imageOfTeam)
    knownFacesPresence = [False] * len(analytics)
    unknownFaceIsPresent = False

    # Find faces in test image
    faceLocations = face_recognition.face_locations(image_to_mark)
    faceEncodings = face_recognition.face_encodings(image_to_mark, faceLocations);

    # Convert to PIL format 
    pilImage = Image.fromarray(image_to_mark)

    # Create a ImageDraw instance

    draw = ImageDraw.Draw(pilImage)

    # Loop through faces in test image
    for(top, right, bottom, left), faceEncoding in zip(faceLocations, faceEncodings):
        matches = face_recognition.compare_faces(knownFaceEncodings, faceEncoding, 0.55)
        
        for index, match in enumerate(matches):
            # Pass already recognized faces
            if knownFacesPresence[index]:
                continue
            analytics[index] = analytics[index] + match
            knownFacesPresence[index] = match
        # If not match Draw Box
        if not any(matches):
            draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0), width=5)
            unknownFaceIsPresent = True

    del draw

    if unknownFaceIsPresent:
        return pilImage
    
    return None
