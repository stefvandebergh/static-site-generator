import os
import shutil

def copy_static_to_public(source_dir, destination_dir):
    if not (source_dir and os.path.exists(source_dir)):
        raise ValueError(f"Source directory '{source_dir}' does not exist.")
    if destination_dir and os.path.exists(destination_dir):
        clear_directory(destination_dir)
    os.mkdir(destination_dir)
    
    copy_static_to_public_r(source_dir, destination_dir)
    

def copy_static_to_public_r(source_dir, destination_dir):
    items = os.listdir(source_dir)
    for item in items:
        if os.path.isfile(os.path.join(source_dir, item)):
            shutil.copy(os.path.join(source_dir, item), os.path.join(destination_dir, item))
        else:
            os.mkdir(os.path.join(destination_dir, item))
            copy_static_to_public_r(os.path.join(source_dir, item), os.path.join(destination_dir, item))

def clear_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)