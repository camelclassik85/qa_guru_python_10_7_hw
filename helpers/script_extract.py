import shutil
from zipfile import ZipFile
from helpers.directory import EXTRACTED_RESOURCES, ARCHIVE_DIRECTORY


def extract_files_from_archive():
    with ZipFile("../archive/test_zip.zip") as new_unzip:
        new_unzip.extractall(EXTRACTED_RESOURCES)


def delete_directories():
    shutil.rmtree(EXTRACTED_RESOURCES)
    shutil.rmtree(ARCHIVE_DIRECTORY)
