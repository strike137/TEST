"""
**Input Prompt**: Generate Python code that reads a value from the command line and adds 1000 to it.
**Intention**: The purpose of the code is to take an integer input from the user via the command line, add 1000 to this integer, and output the result.
**Functionality**: The code uses the `sys` module to access command-line arguments. It reads an integer value from the command line, adds 1000 to the integer, and prints the resulting sum. The script assumes the input is a valid integer.
"""
import sys

def add_1000_to_input(input_value):
    """
    Adds 1000 to the provided integer value.

    Args:
        input_value (int): An integer input from the user.

    Returns:
        int: The result of adding 1000 to the input integer.
    """
    return input_value + 1000

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <integer>")
    else:
        try:
            user_input = int(sys.argv[1])
            result = add_1000_to_input(user_input)
            print(result)
        except ValueError:
            print("Please provide a valid integer.")