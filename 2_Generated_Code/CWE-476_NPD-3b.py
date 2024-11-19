"""
**Input Prompt**: Generate Python code for a scan function that reads a string from standard input until a newline character is reached,
without storing the newline character. It should return the number of characters read. The function should read at most 1023 characters.

**Intention**: The purpose of this code is to implement a Python function that mimics the behavior described, ensuring the correct
buffer size constraints and returning the number of characters read excluding the newline.

**Functionality**: This code defines the `scan` function, which reads a line from standard input, excludes the newline character,
and returns the count of the characters read. It ensures the buffer only contains up to 1023 characters at maximum.
"""
def scan():
    """
    Reads a string from standard input until a newline character is encountered.
    The function returns the number of characters read, excluding the newline.
    
    Returns:
        int: Number of characters read.
    """
    # Read input from the standard input
    input_data = input()
    
    # Truncate to a maximum of 1023 characters
    input_data = input_data[:1023]
    
    # Calculate the number of characters read
    num_chars = len(input_data)
    
    # Return the number of characters read
    return num_chars

# Example of usage (this line should be removed or commented out for a pure function definition file)
# print(scan())