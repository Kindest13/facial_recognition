import cv2
from PIL import ImageGrab
from utils_faces.save_faces import saveFaces

teamPath = './team/team.jpg'
firstTeamSnap = ImageGrab.grab()
# firstTeamSnap.show()
firstTeamSnap.save(teamPath)

teamImage = cv2.imread(teamPath)
saveFaces(teamImage)
