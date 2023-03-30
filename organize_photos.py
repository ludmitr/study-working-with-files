import os


def main():
    os.chdir("Photos")  # change dir

    originals = os.listdir()
    originals = [original for original in originals if original[-4:] == ".jpg"]
    places = [extract_place(file_name) for file_name in originals if extract_place(file_name)]
    places = list(set(places))  # removing duplicates

    # making forlders and sorting photos in folders according its places
    make_place_directories(places)
    move_photos_to_place_folder(originals)


def move_photos_to_place_folder(photos: list):
    for photo in photos:
        folder_name = extract_place(photo)
        new_path = os.path.join(folder_name, photo)  # using relative path
        os.rename(photo, new_path)

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
