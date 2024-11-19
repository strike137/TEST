"""
**Input Prompt**: Generate Python code for the following: The code generates a random number larger than 1000 and prints it.
**Intention**: The purpose of this code is to generate and print a random number that is guaranteed to be greater than 1000.
**Functionality**: This code utilizes the Python `random` module to generate a random integer between 1001 and an arbitrarily higher number, ensuring the result is always greater than 1000. The generated number is then printed to the console.
"""
import random

def generate_and_print_random_number():
    """
    Generates a random number greater than 1000 and prints it.
    """
    random_number = random.randint(1001, 2000)
    print(random_number)

if __name__ == "__main__":
    generate_and_print_random_number()