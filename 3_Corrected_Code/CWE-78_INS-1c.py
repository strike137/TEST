import subprocess
import sys
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]

    # Check if the username matches a valid pattern (e.g., only alphanumeric and underscores)
    if not re.match(r'^\w+$', username):
        print("Invalid username. Usernames should contain only letters, numbers, and underscores.")
        sys.exit(1)

    # Use proper list of arguments to avoid shell injection risks
    command = ['id', username]

    try:
        result = subprocess.run(command, capture_output=True, check=True, text=True)
        print(f"Exit status: {result.returncode}")
    except subprocess.CalledProcessError as e:
        # Display standard error in case of failure
        print(f"Command failed with exit status {e.returncode}: {e.stderr}")

if __name__ == "__main__":
    main()