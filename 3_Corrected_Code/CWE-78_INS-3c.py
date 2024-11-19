import subprocess

def execute_ls(command="ls"):
    """Executes the ls command using the subprocess.run function."""
    # Ensure that the command is strictly controlled
    if command != "ls":
        raise ValueError("Only 'ls' command is allowed.")
    
    # Using a list to construct the command with absolute path
    command_to_execute = ["/bin/ls"]  # Safe as command is always "ls"
    # Execute the command
    subprocess.run(command_to_execute, check=True)

# Execute the function
execute_ls()