import os


def main():
    current_folder = os.getcwd()
    photos_folder = current_folder + "\Photos"

    # creating list of cities for places photos been taken

    file_names = get_file_names(photos_folder)
    cities = [f_name.split("_", 2)[1] for f_name in file_names]
    cities = list(set(cities)) # removing_duplicates

    create_new_folders(current_folder, cities)


if __name__ == '__main__':
    main()


def move_file(old_path, new_path):
    pass


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
