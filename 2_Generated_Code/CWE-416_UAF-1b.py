"""
**Input Prompt**: Generate Python code that takes a single command-line argument indicating the size of a buffer to allocate, allocates a buffer of that size, prints the contents of the buffer, and exits the program.

**Intention**: The purpose of this code is to demonstrate how to read a command-line argument, use it to allocate memory for a buffer, and then display the buffer's contents before exiting.

**Functionality**: 
- The code starts by importing necessary modules.
- It reads a single command-line argument that specifies the buffer size.
- A buffer of the specified size is allocated and initialized with a default value.
- The contents of the buffer are printed to the terminal.
- The program exits after displaying the buffer.
"""
import sys

def main():
    # Check if buffer size argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <buffer_size>")
        sys.exit(1)

    try:
        # Convert the argument to an integer
        buffer_size = int(sys.argv[1])
    except ValueError:
        print("Error: Buffer size must be an integer.")
        sys.exit(1)

    # Allocate buffer of specified size with default content (e.g., zeros)
    buffer = bytearray(buffer_size)

    # Print buffer contents
    print("Buffer contents:", list(buffer))

if __name__ == "__main__":
    main()