import os
import shutil


def main():
    current_folder_path = os.getcwd()
    photos_folder_path = current_folder_path + "\Photos"

    # creating list of cities for places photos been taken
    file_names = get_file_names(photos_folder_path)
    cities = [f_name.split("_", 2)[1] for f_name in file_names]
    cities_without_duplicates = list(set(cities)) # removing_duplicates

    create_new_folders(current_folder_path,
                       cities_without_duplicates)

    # moving photos from folder Photos to folders inside project with
    # matching city name
    for i in range(len(file_names)):
        file_name = f"\\{file_names[i]}"
        old_path = photos_folder_path + file_name
        new_path = current_folder_path + "\\" + cities[i] + file_name
        move_file(old_path, new_path)


def move_file(old_path, new_path):
    shutil.move(old_path, new_path)


def get_file_names(path: str) -> list:
    """create and return list with all files names in path"""
    files = [f for f in os.listdir(path)
             if os.path.isfile(os.path.join(path, f))]
    return files


def create_new_folders(path, folder_names):
    for folder in folder_names:
        final_directory = os.path.join(path, folder)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)


if __name__ == '__main__':
    main()
