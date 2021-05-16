import face_recognition
import shutil, os

from mark_unknown import markUnknownFaces
from mark_presence import markPresenceAnalysis
from send_analytics import sendAnalytics
from utils.create_folder import createFolder




def moveSnapshots():
    originDir = './analytics'
    snapshotsDir = './snapshots'
    destDir = createFolder(originDir, '1', False)

    files = [f.name for f in os.scandir(snapshotsDir) if f.is_file()]

    for file in files:
        filePath = os.path.join(snapshotsDir, file)
        shutil.move(filePath, destDir)

    return destDir



    
def analytics(email):
    originDir = moveSnapshots()
    emailDir = createFolder('./email', '1', False)

    imageOfTeam = face_recognition.load_image_file('./team/team.jpg')

    # team_face_locations = face_recognition.face_locations(imageOfTeam)
    teamFaceEncodings = face_recognition.face_encodings(imageOfTeam)
    faceAnalytics = [0] * len(teamFaceEncodings)

    files = [f.name for f in os.scandir(originDir) if f.is_file()]

    for file in files:
        # Read the image
        filePath = os.path.join(originDir, file)
        unknownImage = face_recognition.load_image_file(filePath)

        markedImage = markUnknownFaces(unknownImage, faceAnalytics)
        if markedImage:
            pathToSave = os.path.join(emailDir, file)
            markedImage.save(pathToSave)
        

    markedAnalysisImage = markPresenceAnalysis(faceAnalytics, len(files))
    markedAnalysisImage.save(os.path.join(emailDir, 'analytics.jpg'))
    sendAnalytics(emailDir, email)

    # clear memory
    shutil.rmtree(originDir)
    shutil.rmtree(emailDir)
