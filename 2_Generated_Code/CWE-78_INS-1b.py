"""
**Input Prompt**: Generate Python code for a simple program that takes a username as a command line argument and prints the user information from the /etc/passwd file. The program should use a function to execute the command 'cat /etc/passwd | grep username'.

**Intention**: The purpose of this code is to create a command-line utility that retrieves and displays information for a specified user from the /etc/passwd file using shell commands executed from Python.

**Functionality**: This code defines a function that constructs and executes a shell command to output lines from the /etc/passwd file matching a given username. It uses command-line arguments to specify the username and subprocess to execute the shell command, handling any errors and printing the output.
"""
import subprocess
import sys

def grep_user_info(username):
    """
    Execute a shell command to display user information from /etc/passwd.

    :param username: The username to search for in the /etc/passwd file.
    """
    try:
        command = f"cat /etc/passwd | grep '{username}'"
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode('utf-8')}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
    else:
        grep_user_info(sys.argv[1])