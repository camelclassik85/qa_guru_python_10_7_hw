import os
from zipfile import ZipFile
from helpers.directory import RESOURCES_PATH, ARCHIVE_DIRECTORY
from glob import glob


def add_files_to_archive():
    if not os.path.exists(ARCHIVE_DIRECTORY):
        os.mkdir(ARCHIVE_DIRECTORY)
    with ZipFile("../archive/test_zip.zip", 'w') as new_zip:
        for file in glob(os.path.join(RESOURCES_PATH, '*')):
            new_zip.write(file, os.path.basename(file))
