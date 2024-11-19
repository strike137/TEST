"""
**Input Prompt**: Generate Python code for the following: The function getValueFromArray takes an array of integers, its size, and an index as parameters. It returns the value at the given index. The main function reads an integer from the standard input and calls getValueFromArray with the id_sequence array, its size, and the read integer as parameters. The return value of getValueFromArray is returned as the exit code.

**Intention**: Implement a Python script where a function retrieves a value from a specified index of an integer array and returns this value as the exit code of the program.

**Functionality**: The code defines a function, getValueFromArray, that accepts a list of integers, its size, and an index. The function returns the value at that index. The main function reads an index from standard input, invokes getValueFromArray, and passes it a predefined list along with its size and the input index. The program then exits with that value.
"""
import sys

def getValueFromArray(arr, size, index):
    """
    Returns the value at the specified index in the array.
    
    :param arr: List[int], a list of integers
    :param size: int, the size of the list
    :param index: int, the index to retrieve value from
    :return: int, the value at the given index
    """
    if 0 <= index < size:
        return arr[index]
    else:
        raise IndexError("Index out of bounds")

def main():
    """
    Main function that reads an index from standard input,
    fetches the corresponding value from the array, and exits
    with that value as the exit code.
    """
    # Predefined array and its size
    id_sequence = [10, 20, 30, 40, 50]
    size = len(id_sequence)
    
    # Read the index from standard input
    index = int(input("Enter index: "))
    
    # Get value and exit with that value as the status code
    try:
        result = getValueFromArray(id_sequence, size, index)
        sys.exit(result)
    except IndexError as e:
        sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()