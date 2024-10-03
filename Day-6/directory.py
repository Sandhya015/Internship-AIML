import os

def file_system_operations()->dict:
    current_directory =os.getcwd()

    files_in_directory =os.listdir(current_directory)

    new_folder_path =os.path.join(current_directory,'new_folder')

    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
        confirmation_message="'new_folder' directory has been created"
    else:
        confirmation_message="'new_folder'directory already exist"

    result ={
        "current_directory":current_directory,
        "files_in_directory":files_in_directory,
        "confirmation_message":confirmation_message
    }

    return result