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

    im = ImageGrab.grab()
    # im.show()
    my_path_to_file = root / "snapshots" / f'{name}.jpg'

    im.save(my_path_to_file)
