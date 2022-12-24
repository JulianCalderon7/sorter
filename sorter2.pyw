import os

WORKING_DIRECTORY = r"C:\Users\gonza\Downloads"
FILE_MAP = (
    ("Pictures", (".jpeg", ".jpg", ".png", ".ico")),
    ("Documents", (".pdf", ".pptx", ".log", ".docx", ".txt")),
    ("Audio", (".mp3", ".wav")),
    ("Video", (".mp4", ".avi")),
    ("Compressed", (".zip", ".rar", ".7z")),
    ("Executables", (".msi", ".exe")),
    ("Torrents", (".torrent")),
    ("Code", (".py", ".c", ".h", ".st")),
)


def sort_file(file: str) -> None:
    print(f"sorting file {file}")


def should_sort(file: str) -> bool:
    return not os.path.isdir(file)


os.chdir(WORKING_DIRECTORY)
for file in os.listdir():
    if should_sort(file):
        sort_file(file)
