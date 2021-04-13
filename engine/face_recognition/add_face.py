import face_recognition as f
import cv2
import sys
from pathlib import Path
import _pickle as c

root = Path(".")
myPath = root / "faces"

s, img, name = sys.argv
if img != "cam":
    imgArray = f.load_image_file(img)
    faceEnc = f.face_encodings(imgArray)[0]
    with open(myPath / name, 'wb') as fp:
        c.dump(faceEnc, fp)

if img == "cam":
    cam = cv2.VideoCapture(0)
    while True:
        _, imgArray = cam.read()
        cv2.imshow("Press 'a' to add your face", imgArray)
        k = cv2.waitKey(10)
        if k == ord('a'):
            faceEnc = f.face_encodings(imgArray)[0]
            with open(myPath / name, 'wb') as fp:
                c.dump(faceEnc, fp)
            break
    cam.release()
    cv2.destroyAllWindows()
