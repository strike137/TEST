"""
**Input Prompt**: Generate Python code that takes a username as a command line argument, executes the 'id <username>' command, and prints the exit status of the command.
**Intention**: To create a script that can check user information by taking a username input, running the relevant system command to fetch user details, and then reporting whether the command executed successfully or not.
**Functionality**: The code utilizes the subprocess module to execute the 'id' command with the provided username. It captures and prints out the command's exit status. An exit status of 0 indicates success, while any other value indicates a failure in execution.
"""
import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    result = subprocess.run(['id', username], capture_output=True)
    print(f"Exit status: {result.returncode}")

if __name__ == "__main__":
    main()