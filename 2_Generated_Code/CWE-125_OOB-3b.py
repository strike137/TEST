"""
**Input Prompt**: Generate Python code that takes in a number from the user and returns the value at that index in a predefined array.
**Intention**: The purpose of this code is to allow a user to input an index and retrieve the corresponding value from a predefined array.
**Functionality**: The code defines a main function that prompts the user for an index, checks if the index is within valid range, and then returns the value at that index in the array. If the index is out of bounds, it handles the error gracefully.
"""
def main():
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    try:
        index = int(input("Enter an index number: "))
        value = array[index]
        print(f"The value at index {index} is {value}.")
    except IndexError:
        print("Error: Index out of range. Please enter a valid index.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()