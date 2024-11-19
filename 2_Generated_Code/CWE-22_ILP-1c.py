"""
**Input Prompt**: Generate Python code for the following:
The code reads the requested file from the safe directory.

**Intention**: The purpose is to create a Python script that securely reads a file from a specified directory 
by ensuring the file path points within a designated "safe" directory to prevent unauthorized file access.

**Functionality**: The code defines a function `read_file_from_safe_directory` that takes two parameters: the 
path to the file and the safe directory path. It checks if the file path resides within the specified safe directory 
to avoid directory traversal vulnerabilities. If the file is within the safe directory, it reads and returns the file's content. 
Otherwise, it raises an exception indicating the file cannot be accessed.
"""
import os

def read_file_from_safe_directory(file_path: str, safe_directory: str) -> str:
    """
    Reads a file from the safe directory if it exists within it, otherwise raises an exception.

    :param file_path: The path to the file to be read.
    :param safe_directory: The path to the safe directory to enforce file access restrictions.
    :return: The content of the file as a string.
    :raises ValueError: If the file is outside the safe directory.
    """
    # Get absolute paths for safety check
    absolute_file_path = os.path.abspath(file_path)
    absolute_safe_directory = os.path.abspath(safe_directory)

    # Check if file is inside the safe directory
    if not absolute_file_path.startswith(absolute_safe_directory):
        raise ValueError(f"Access denied: {file_path} is outside the safe directory.")

    # Read and return file contents
    with open(absolute_file_path, 'r') as file:
        return file.read()

# Example usage
if __name__ == "__main__":
    safe_dir = "/path/to/safe/directory"
    file_name = "example.txt"
    try:
        content = read_file_from_safe_directory(file_name, safe_dir)
        print("File Content:")
        print(content)
    except Exception as e:
        print(f"Error: {e}")