import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)
            # Using filepath.name removes the whole path while creating compressed folders. like C:/Users/etc.


if __name__ == "__main__":
    make_archive(filepaths=["bonus1.py", "bonus2.py"], dest_dir="dest")
