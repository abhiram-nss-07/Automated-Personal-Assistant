import os

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def read_lines_from_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def write_lines_to_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)
