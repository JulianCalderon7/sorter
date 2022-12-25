import os


DIRECTORY = r"C:\Users\gonza\Downloads"
TYPE_MAP = (
    ("Pictures", (".jpeg", ".jpg", ".png", ".ico")),
    ("Documents", (".pdf", ".pptx", ".log", ".docx", ".txt")),
    ("Audio", (".mp3", ".wav")),
    ("Video", (".mp4", ".avi")),
    ("Compressed", (".zip", ".rar", ".7z")),
    ("Executables", (".msi", ".exe")),
    ("Torrents", (".torrent")),
    ("Code", (".py", ".c", ".h", ".st")),
)


def sort_directory(directory: str):
    """
    Sorts all files from working directory into subdirectories, by file extension
    """
    for file in os.scandir(directory):
        if should_sort(file):
            sort_file(file)


def sort_file(file: os.DirEntry):
    """
    Sorts file into corresponding subfolder
    File should be sortable
    """
    subfolder_path = subfolder_for_file(file)
    if subfolder_path == None:
        return

    new_path = os.path.join(subfolder_path, file.name)
    move(file.path, new_path)


def subfolder_for_file(file: os.DirEntry) -> str:
    """
    Returns subdirectory for given file
    Directory is created if needed
    """

    parent_dir = os.path.dirname(file.path)
    extension = os.path.splitext(file.name)[1]

    category = get_folder_for_extension(extension)
    if category == None:
        return None

    category_path = os.path.join(parent_dir, category)
    if not os.path.isdir(category_path):
        os.mkdir(category_path)

    return category_path


def get_folder_for_extension(extension: str) -> str:
    """
    Returns subfolder name for given file extension
    Returns None on unknown extension
    """
    for category in TYPE_MAP:
        if extension.lower() in category[1]:
            return category[0]


def should_sort(file: os.DirEntry) -> bool:
    """
    Returns true if file should be sorted by sorter
    """
    return not file.is_dir()


def move(source: str, destination: str):
    """
    Moves file from source into destination
    If file exists, it add a trailing (n) to the file name.
    """

    name, extension = os.path.splitext(destination)

    i = 2
    while os.path.exists(destination):
        destination = f"{name} ({i}){extension}"
        i += 1

    os.rename(source, destination)


sort_directory(DIRECTORY)
