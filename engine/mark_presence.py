import face_recognition
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from utils.get_color import getColor

def markPresenceAnalysis(analytics, images_length):
    image_of_team = face_recognition.load_image_file('./team/team.jpg')

    face_locations = face_recognition.face_locations(image_of_team)
    face_encodings = face_recognition.face_encodings(image_of_team, face_locations);

    # Convert to PIL format 
    pil_image = Image.fromarray(image_of_team)

    # Create a ImageDraw instance

    draw = ImageDraw.Draw(pil_image)
    
    font_path = "./fonts/OpenSans-Bold.ttf"
    font = ImageFont.truetype(font_path, 16)

    # Loop through faces in test image
    for index, (top, right, bottom, left) in enumerate(face_locations):
        presence_percentage = int(analytics[index] * 100 / images_length)
        color = getColor(presence_percentage)
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=color)
        # Draw a label with a name below the face
        text_percentage = f'{presence_percentage}%'
        text_width, text_height = draw.textsize(text_percentage)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=color, outline=color)
        draw.text((left + 6, bottom - text_height - 10), text_percentage, fill=(255, 255, 255, 255), font=font)

    del draw

    pil_image.save('./email/analytics.jpg')
