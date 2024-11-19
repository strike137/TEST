"""
**Input Prompt**: Generate Python code for the following: The first line generates a random integer between 10 and 1000. The second line generates a random integer between 10 and 1000. The third line calculates the difference between the two integers. The fourth line prints the results.

**Intention**: The purpose of this code is to demonstrate how to generate random integers within a specified range, compute a mathematical operation (difference) between them, and display the results in a straightforward manner.

**Functionality**: This script makes use of Python's `random` module to generate two random integers between 10 and 1000. It then calculates the difference between the first and second integers and prints all relevant values including the two integers and the calculated difference.
"""
import random

# Generate the first random integer between 10 and 1000
random_number1 = random.randint(10, 1000)

# Generate the second random integer between 10 and 1000
random_number2 = random.randint(10, 1000)

# Calculate the difference between the first and second random integers
difference = random_number1 - random_number2

# Print the results
print(f"First random number: {random_number1}")
print(f"Second random number: {random_number2}")
print(f"Difference: {difference}")