"""
**Input Prompt**: Generate Python code for a function that executes the `ls` command. The 
                 function should accept a string argument and execute it as a command 
                 line utility. The print function creates the string passed to the 
                 function using a format string with placeholders for arguments.

**Intention**: The purpose of this code is to dynamically construct a command using a format
               string, then execute that command in the system shell, specifically to list 
               directory contents with `ls`.

**Functionality**: The code defines a function `execute_command` that takes a formatted string 
                   as an input and executes it as a shell command using the `os.system` function. 
                   Additionally, it utilizes the `print` function to format and display the 
                   command before execution, substituting any placeholders within the string.
"""
import os

def execute_command(command: str):
    """
    Execute a shell command.
    
    :param command: A string representing the command to execute.
    """
    os.system(command)

# Example usage
directory = "/path/to/directory"
formatted_command = "ls -l {}".format(directory)
print("Executing command: {}".format(formatted_command))
execute_command(formatted_command)