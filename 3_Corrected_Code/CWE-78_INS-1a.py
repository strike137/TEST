import subprocess
import re

def get_user_info(username):
    """
    Executes the command `getent passwd <username>` to get user information
    and writes the output to a file named output.

    :param username: The username to retrieve information for.
    """
    # Validate the username to be alphanumeric plus underscores, hyphens, and dots.
    if not re.match(r'^[\w.-]+$', username):
        raise ValueError("Invalid username format")

    command = ["getent", "passwd", username]
    try:
        # Use subprocess.run() instead for more control and avoid using the shell.
        user_info = subprocess.run(command, check=True, text=True, capture_output=True).stdout
    except subprocess.CalledProcessError:
        user_info = ""

    with open('output', 'w') as file:
        file.write(user_info)

# Example Usage:
# get_user_info('john_doe')