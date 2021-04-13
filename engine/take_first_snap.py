import cv2
from PIL import ImageGrab
from utils_faces.save_faces import saveFaces

team_path = './team/team.jpg'
first_team_snap = ImageGrab.grab()
# first_team_snap.show()
first_team_snap.save(team_path)

team_image = cv2.imread(team_path)
saveFaces(team_image)
