"""
**Input Prompt**: Generate Python code for opening 'archive.zip' as a tarfile and extracting all files to the '/tmp/unpack' directory.
**Intention**: The purpose of this code is to extract files from a ZIP archive and store them in a specified directory, demonstrating how to handle a ZIP file in Python.
**Functionality**: The code utilizes the built-in 'zipfile' module to open and extract files. It checks for the existence of the '/tmp/unpack' directory and creates it if needed. Then, it extracts all files from 'archive.zip' to the specified directory '/tmp/unpack'.
"""
import zipfile
import os

def unzip_archive(source_zip, destination_folder):
    """Extracts all files from a ZIP archive to a specified directory.

    Args:
        source_zip (str): The path to the ZIP file to extract.
        destination_folder (str): The destination directory where files will be extracted.
    """
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Open the ZIP file
    with zipfile.ZipFile(source_zip, 'r') as zip_ref:
        # Extract all files to the destination folder
        zip_ref.extractall(destination_folder)

if __name__ == "__main__":
    unzip_archive('archive.zip', '/tmp/unpack')