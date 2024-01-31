import pytest
from helpers.script_zip import add_files_to_archive
from helpers.script_extract import extract_files_from_archive, delete_directories


@pytest.fixture(scope="session", autouse=True)
def add_data_for_test():
    add_files_to_archive()
    extract_files_from_archive()

    yield

    delete_directories()
