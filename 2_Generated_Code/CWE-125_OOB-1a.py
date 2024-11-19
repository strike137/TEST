"""
**Input Prompt**: Generate Python code for the following: The function getValueFromArray takes an array of integers;
its size and an index as parameters. It returns the value at the given index. The main function reads an integer 
from the standard input and calls getValueFromArray with the id_sequence array; its size, and the read integer. 
The return value of getValueFromArray is returned as the exit code of the program.

**Intention**: The purpose of this code is to implement a function that retrieves a value from a specific index of 
an integer array and use this function to return the value as an exit code of the program by reading an index from 
standard input.

**Functionality**: The code defines a function, `getValueFromArray`, which takes three arguments: an array, its size, 
and an index. It returns the value at the specified index. The `main` function reads an integer index from the user, 
calls `getValueFromArray` using a predefined array `id_sequence`, and exits the program with the value at that index 
as the status code if the index is in bounds. If the index is out of bounds, it exits with status code 1.
"""
import sys

def getValueFromArray(arr, size, index):
    """
    Retrieves a value from the array at the specified index.

    :param arr: List of integers.
    :param size: Size of the array.
    :param index: Index of the desired value in the array.
    :return: Value at the specified index of the array.
    """
    if 0 <= index < size:
        return arr[index]
    else:
        print("Index out of bounds")
        return None

def main():
    id_sequence = [10, 20, 30, 40, 50]  # Example array
    size = len(id_sequence)

    try:
        index = int(input("Enter index: "))
        value = getValueFromArray(id_sequence, size, index)
        
        if value is not None:
            sys.exit(value)
        else:
            sys.exit(1)
    except ValueError:
        print("Invalid input")
        sys.exit(1)

if __name__ == "__main__":
    main()