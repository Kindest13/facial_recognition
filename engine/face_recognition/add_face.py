import face_recognition as f
import cv2
import sys
from pathlib import Path
import _pickle as c

root = Path(".")
my_path = root / "faces"

s, img, name = sys.argv
if img != "cam":
    img_array = f.load_image_file(img)
    face_enc = f.face_encodings(img_array)[0]
    with open(my_path / name, 'wb') as fp:
        c.dump(face_enc, fp)
    print ("Done")

if img == "cam":
    cam = cv2.VideoCapture(0)
    while True:
        _, img_array = cam.read()
        cv2.imshow("Press 'a' to add your face", img_array)
        k = cv2.waitKey(10)
        if k == ord('a'):
            face_enc = f.face_encodings(img_array)[0]
            print(face_enc)
            with open(my_path / name, 'wb') as fp:
                c.dump(face_enc, fp)
            break
    print ("Done")
    cam.release()
    cv2.destroyAllWindows()
