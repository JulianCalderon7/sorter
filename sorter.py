from pathlib import Path
import argparse
import json
from typing import Dict, List

from utils import move_file_to_folder

SHOULD_IGNORE = ["desktop.ini"]


def default_mappings() -> Path:
    return Path(__file__).parent / "mappings.json"


def setup_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="sorter",
        description="""
        Sorts all non-directory files in a folder into subfolders based on
        their extension. If there are duplicate files, they will be renamed
        to avoid overwriting.
        """,
        epilog="by Julian Gonzalez Calderon",
    )
    parser.add_argument("folder", help="folder to sort", type=Path)
    parser.add_argument(
        "-m",
        "--mapping",
        help="custom JSON file containing extension mappings",
        default=default_mappings(),
        type=Path,
    )

    return parser.parse_args()


class Mapper:
    """
    Maps file extensions to categories, based on a JSON file."""

    def __init__(self, mappings: Path):
        self.mappings: Dict[str, str] = {}

        for category, extensions in self.load_mappings(mappings).items():
            for extension in extensions:
                self.mappings[extension] = category

    def load_mappings(self, mappings: Path) -> Dict[str, List[str]]:
        with open(mappings) as f:
            return json.load(f)

    def get_category(self, file: Path) -> None | str:
        return self.mappings.get(file.suffix.lower())


class Sorter:
    def __init__(self, folder: Path, mappings: Path):
        self.folder = folder
        self.mapper = Mapper(mappings)

    def should_ignore(self, file_path: Path) -> bool:
        return file_path.name in SHOULD_IGNORE or file_path.is_dir()

    def sort(self):
        for file in self.folder.iterdir():
            if self.should_ignore(file):
                continue
            if category := self.mapper.get_category(file):
                self.move_file_to_category(file, category)

    def move_file_to_category(self, file: Path, category: str):
        move_file_to_folder(file, self.folder / category)


def main(args: argparse.Namespace):
    sorter = Sorter(args.folder, args.mapping)
    sorter.sort()


if __name__ == "__main__":
    args = setup_parser()
    main(args)
