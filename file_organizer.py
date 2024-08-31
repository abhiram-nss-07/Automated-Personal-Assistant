import os
import shutil
import config
from utils.helper import create_folder_if_not_exists

def organize_files():
    for filename in os.listdir(config.TARGET_DIRECTORY):
        if filename.startswith('.'):
            continue

        file_path = os.path.join(config.TARGET_DIRECTORY, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            moved = False
            for category, extensions in config.FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(config.TARGET_DIRECTORY, category)
                    create_folder_if_not_exists(category_folder)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved {filename} to {category}")
                    moved = True
                    break
            
            if not moved:
                others_folder = os.path.join(config.TARGET_DIRECTORY, "Others")
                create_folder_if_not_exists(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved {filename} to Others")
