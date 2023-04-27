from pathlib import Path


def move_file_to_folder(file: Path, destination_folder: Path):
    if not destination_folder.exists():
        destination_folder.mkdir()

    desired = destination_folder / file.name
    actual = _name_for(desired)
    file.rename(actual)


def _name_for(desired: Path) -> Path:
    counter = 1
    destination = desired
    while destination.exists():
        counter += 1
        destination = _destination_for_duplicate(desired, counter)

    return destination


def _destination_for_duplicate(desired: Path, counter: int) -> Path:
    return desired.with_stem(f"{desired.stem} ({counter})")
