import sys
import time
import datetime

from PIL import ImageGrab
from pathlib import Path


def getDateTime(time):
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d(%H-%M-%S)')


def takeSnapshot():
    print("I'm working...")
    root = Path(".")

    tm = time.time()
    name = getDateTime(tm)

    snapshot = ImageGrab.grab()
    rgb_snapshot = snapshot.convert('RGB')
    # snapshot.show()
    myPathToFile = root / "snapshots" / f'{name}.jpg'

    rgb_snapshot.save(myPathToFile)
