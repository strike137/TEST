"""
**Input Prompt**: Generate Python code for the following: A function takes in command line arguments. 
Command line arguments are an array of strings; each string is one of the arguments that was passed to 
the program. The code should return the value at the index provided in argv[1].

**Intention**: The purpose of this code is to read command line arguments, and based on the value passed 
as the second command line argument (argv[1]), return the argument found at that index in the argument list.

**Functionality**: This script uses the sys module to access command line arguments. It reads the value at 
argv[1], converts it to an integer, and then uses this integer to index into the list of arguments. The 
script finally prints the argument found at that index.
"""
import sys

def get_argument_at_index():
    if len(sys.argv) < 3:
        print("Error: Not enough arguments provided.")
        return None
    try:
        index = int(sys.argv[1])
        argument = sys.argv[index]
        return argument
    except (ValueError, IndexError) as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    result = get_argument_at_index()
    if result:
        print(result)