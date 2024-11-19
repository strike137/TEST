"""
**Input Prompt**: Generate Python code for a program where the user is prompted to enter an index 
of a vehicle. The user's input is converted to an integer and used to access an array of vehicles. 
The program then prints the vehicle at the specified index.

**Intention**: The purpose of this code is to prompt the user for an index, convert it to an integer, 
retrieve the corresponding vehicle from a predefined list, and print the vehicle's name.

**Functionality**: The code first defines a list of vehicles. It then prompts the user to input an index, 
converts this input from a string to an integer, and uses this integer to access the list of vehicles. 
Finally, it prints the vehicle at the specified index. The code assumes the input is valid and that 
the index is within the range of the list.
"""
def main():
    vehicles = ['Car', 'Bike', 'Truck', 'Boat', 'Airplane']
    try:
        index = int(input("Enter the index of the vehicle (0-4): "))
        if 0 <= index < len(vehicles):
            print(f"The vehicle at index {index} is: {vehicles[index]}")
        else:
            print("Index out of range. Please enter a valid index between 0 and 4.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()