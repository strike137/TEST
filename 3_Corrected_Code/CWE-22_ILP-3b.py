import os
import zipfile
import tempfile
import shutil

# File path for the zip file and destination directory
zip_file_path = 'archive.zip'

# Create a secure temporary directory
with tempfile.TemporaryDirectory() as destination_directory:
    # Open the zip file and extract its contents
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)
    
    # Perform any additional operations on the extracted files as needed
    # For example, copy the extracted files to a desired location
    final_destination = '/desired/location'
    # Ensure the final destination directory exists before copying
    os.makedirs(final_destination, exist_ok=True)
    for item in os.listdir(destination_directory):
        s = os.path.join(destination_directory, item)
        d = os.path.join(final_destination, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)