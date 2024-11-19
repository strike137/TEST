"""
**Input Prompt**: Generate Python code that uses a system function to execute the `ls` command. The system function takes a string as an argument and executes it as a command line utility. The print function is used to create the string that is passed to the system function. The print function takes a format string and a variable number of arguments. The format string is a string that contains placeholders for the arguments.

**Intention**: The purpose of this code is to demonstrate executing a shell command from within a Python script using the `os.system` function. It builds and executes the `ls` command by using string formatting.

**Functionality**: This script defines a function `execute_ls_command` that uses the `os.system` function from the `os` module to execute the `ls` command. The command string is constructed using string formatting via the `format` method. The function is then called to execute the command and list directory contents.
"""
import os

def execute_ls_command(directory="."):
    """
    Executes the 'ls' command on the specified directory.

    :param directory: The directory to list. Defaults to the current directory.
    """
    command_template = "ls {}"
    command = command_template.format(directory)
    os.system(command)

# Execute the command to list the contents of the current directory
execute_ls_command()