import subprocess
import os
from pathlib import Path

def is_valid_directory(directory: str) -> bool:
    """
    Validates the directory input to prevent command injection risks.
    
    :param directory: The directory string to validate.
    :return: True if the directory is considered safe, False otherwise.
    """
    # Check if directory is an absolute path and does not contain traversal attempts
    path = Path(directory).resolve()
    return path.is_absolute() and '..' not in path.parts and '~' not in path.parts and path.is_dir()

def execute_command(command: list):
    """
    Execute a shell command.
    
    :param command: A list representing the command to execute.
    """
    # Execute the command using a list of arguments
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
directory = "/path/to/directory"
if is_valid_directory(directory):
    formatted_command = ["ls", "-l", directory]
    print("Executing command: ls -l {}".format(directory))
    execute_command(formatted_command)
else:
    print("Invalid directory provided.")