"""
**Input Prompt**: Generate Python code for the following: 
Open the archive.zip file as a tarfile. Extract all files from the archive to the /tmp/unpack directory.

**Intention**: The purpose of this code is to extract all files from a provided zipped archive and save them to a specified directory.

**Functionality**: 
The code opens a zip file named 'archive.zip', reads its contents, and extracts all files into the '/tmp/unpack' directory. It uses the `zipfile` module to handle zip files.

1. Import the `zipfile` module to work with zip archives.
2. Define the path of the zip file and the output directory.
3. Use a context manager to open the zip file.
4. Extract all the contents into the specified directory.
"""
import os
import zipfile

# File path for the zip file and destination directory
zip_file_path = 'archive.zip'
destination_directory = '/tmp/unpack'

# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Open the zip file and extract its contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(destination_directory)