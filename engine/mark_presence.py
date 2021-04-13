import face_recognition
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from utils.get_color import getColor

def markPresenceAnalysis(analytics, images_length):
    imageOfTeam = face_recognition.load_image_file('./team/team.jpg')

    faceLocations = face_recognition.face_locations(imageOfTeam)

    # Convert to PIL format 
    pilImage = Image.fromarray(imageOfTeam)

    # Create a ImageDraw instance

    draw = ImageDraw.Draw(pilImage)
    
    fontPath = "./fonts/OpenSans-Bold.ttf"
    font = ImageFont.truetype(fontPath, 16)

    # Loop through faces in test image
    for index, (top, right, bottom, left) in enumerate(faceLocations):
        presencePercentage = int(analytics[index] * 100 / images_length)
        color = getColor(presencePercentage)
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=color)
        # Draw a label with a name below the face
        textPercentage = f'{presencePercentage}%'
        _, textHeight = draw.textsize(textPercentage)
        draw.rectangle(((left, bottom - textHeight - 10), (right, bottom)), fill=color, outline=color)
        draw.text((left + 6, bottom - textHeight - 10), textPercentage, fill=(255, 255, 255, 255), font=font)

    del draw

    return pilImage
