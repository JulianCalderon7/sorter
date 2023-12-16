import argparse
from pathlib import Path

from utils import move_file_to_folder


def setup_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="flatter",
        description="""
        Flatten a folder structure recursively, into a single folder.
        If there are duplicate files, they will be renamed to avoid overwriting.
        """,
        epilog="by Julian Gonzalez Calderon",
    )
    parser.add_argument("folder", help="folder to flatten", type=Path)
    return parser.parse_args()


class Flatter:
    def __init__(self, folder: Path):
        self.folder = folder

    def inner_flat(self, folder: Path):
        for file in folder.iterdir():
            if file.is_dir():
                self.inner_flat(file)
            else:
                move_file_to_folder(file, self.folder)

        folder.rmdir()

    def flat(self):
        for file in self.folder.iterdir():
            if file.is_dir():
                self.inner_flat(file)


def main(args: argparse.Namespace):
    flatter = Flatter(args.folder)
    flatter.flat()


if __name__ == "__main__":
    args = setup_parser()
    main(args)
