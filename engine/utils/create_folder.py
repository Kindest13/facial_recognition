import os
import shutil

def createFolder(origin_dir, dir_to_create, rewrite):
    destDir = os.path.join(origin_dir, dir_to_create)
    analyticDirs = [d.name for d in os.scandir(origin_dir) if d.is_dir()]

    if rewrite and os.path.exists(destDir):
        shutil.rmtree(destDir)
    elif analyticDirs:
        newFolderName = str(int(max(analyticDirs)) + 1)
        destDir = os.path.join(origin_dir, newFolderName)

    os.mkdir(destDir)

    return destDir
    