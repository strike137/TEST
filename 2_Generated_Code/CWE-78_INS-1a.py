"""
**Input Prompt**: Generate Python code that executes the command `getent passwd <username>` using the system() function and stores the output in a file named output.

**Intention**: The purpose of this code is to retrieve and store the user information for a given username from the system's passwd database.

**Functionality**: The code defines a function named `get_user_info` that takes a `username` as an argument. It constructs a command to retrieve the user information using `getent passwd <username>`. The `os.popen` method is used to execute the command and capture the output. This output is then written to a file named output.
"""
import os

def get_user_info(username):
    """
    Executes the command `getent passwd <username>` to get user information
    and writes the output to a file named output.

    :param username: The username to retrieve information for.
    """
    command = f"getent passwd {username}"
    with os.popen(command) as stream:
        user_info = stream.read()

    with open('output', 'w') as file:
        file.write(user_info)

# Example Usage:
# get_user_info('john_doe')