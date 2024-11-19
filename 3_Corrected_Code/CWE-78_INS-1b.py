import subprocess
import sys
import re
from pathlib import Path

def grep_user_info(username):
    """
    Execute a shell command to display user information from /etc/passwd.

    :param username: The username to search for in the /etc/passwd file.
    """
    # Validate the input to ensure it contains only valid characters for a username
    if not re.match(r'^[a-z_][a-z0-9_-]*[$]?$', username, re.IGNORECASE):
        print("Invalid username provided.", file=sys.stderr)
        return

    try:
        # Construct the command as a list without using shell=True
        # Use constant file path to further enhance security
        passwd_file = Path('/etc/passwd')  # Known path for demonstration
        
        # Check if passwd_file path exists and is a file
        if not passwd_file.is_file():
            print("Password file not found.", file=sys.stderr)
            return

        # It's safe to use subprocess because input is validated and no shell=True
        command = ['grep', username, str(passwd_file)]
        result = subprocess.run(command, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode('utf-8')}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
    else:
        grep_user_info(sys.argv[1])