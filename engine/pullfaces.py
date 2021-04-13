from PIL import Image
from pathlib import Path
import face_recognition

def pullfaces(path, name):
    print("pullfaces")
    root = Path(".")
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    my_path = root / "faceshots" / name
    Path(my_path).mkdir(parents=True, exist_ok=True)

    for face_location in face_locations:
        top, right, bottom, left = face_location

        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        # pil_image.show()
        pil_image.save(my_path / f'{top}.jpg')
