import os
import shutil

def createFolder(origin_dir, dir_to_create, rewrite):
    dest_dir = os.path.join(origin_dir, dir_to_create)
    analytic_dirs = [d.name for d in os.scandir(origin_dir) if d.is_dir()]
    print(analytic_dirs)

    if rewrite and os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    elif analytic_dirs:
        new_folder_name = str(int(max(analytic_dirs)) + 1)
        dest_dir = os.path.join(origin_dir, new_folder_name)

    os.mkdir(dest_dir)

    return dest_dir
    