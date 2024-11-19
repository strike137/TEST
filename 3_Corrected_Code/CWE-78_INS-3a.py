
import os

def execute_ls_command(directory="."):
    """
    Executes the 'ls' command on the specified directory.

    :param directory: The directory to list. Defaults to the current directory.
    """
    try:
        # Execute the 'ls' command using os.system to match the docstring
        os.system(f"ls {directory}")
    except Exception as e:  # Changed OSError to Exception to catch all possible errors from os.system
        print(f"Error: {e}")

# Execute the command to list the contents of the current directory
execute_ls_command()
