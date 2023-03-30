import os

def main():
    os.chdir("Photos")
    originals = os.listdir()
    places = [extract_place(file_name) for file_name in originals]


def extract_place(file_name: str) -> str:
    """Extracts the place from a filename and returns it"""
    return file_name.split("_")[1]


if __name__ == '__main__':
    main()