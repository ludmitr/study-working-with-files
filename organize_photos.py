import os


def main():
    organize_photos("Photos")


def organize_photos(directory):
    old_working_directory = os.getcwd()
    os.chdir(directory)  # change dir

    # getting photos names and places names
    originals_photo_names = os.listdir()
    originals_photo_names = [original for original in originals_photo_names if original[-4:] == ".jpg"]
    places = [extract_place(file_name) for file_name in originals_photo_names if extract_place(file_name)]
    places = list(set(places))  # removing duplicates

    # making folders and sorting photos in folders according its places
    make_place_directories(places)
    move_photos_to_place_folder(originals_photo_names)

    os.chdir(old_working_directory)


def move_photos_to_place_folder(file_names: list):
    for file in file_names:
        folder_name = extract_place(file)
        os.rename(file,
                  os.path.join(folder_name, file))  # using relative path


def make_place_directories(places):
    for place in places:
        place_folder_path = os.path.join(os.getcwd(), place)
        if not os.path.exists(place_folder_path):
            os.mkdir(place)


def extract_place(file_name: str) -> str:
    """Extracts the place from a filename and returns it"""
    if file_name[-3:] == "jpg":  # check if file is an image
        return file_name.split("_")[1]


if __name__ == '__main__':
    main()
