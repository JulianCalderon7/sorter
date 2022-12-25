import os


class Sorter:
    """
    Sorts all files in given folder into subfolders, by file extension
    """

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

    def __init__(self, folder):
        self.path = folder

    def sort(self):
        """ """
        for file in os.scandir(self.path):
            if self.should_sort(file):
                self.sort_file(file)

    def sort_file(self, file: os.DirEntry):
        """
        Sorts file into corresponding subfolder
        File should be sortable
        """
        name, extension = os.path.splitext(file.path)
        category = self.get_folder_for_extension(extension)

        print(f"sorting file {file.name}")

    def get_folder_for_extension(self, extension: str) -> str:
        """
        Returns subfolder name for given file extension
        Returns None on unknown extension
        """
        for category in self.TYPE_MAP:
            if extension.lower() in category[1]:
                return category[0]

    def should_sort(self, file: os.DirEntry) -> bool:
        """
        Returns true if file should be sorted by sorter
        """
        return not file.is_dir()
