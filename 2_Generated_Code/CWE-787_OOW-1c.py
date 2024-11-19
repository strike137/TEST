"""
**Input Prompt**: Generate Python code that uses the rand() function to generate three random float numbers. Convert these numbers to strings and store them in the variables string1, string2, and string3.
**Intention**: The purpose of this code is to demonstrate how to generate random float numbers in Python, convert them to strings, and store them in separate variables.
**Functionality**: The code imports the necessary module to generate random numbers, creates three random float numbers, converts these numbers to strings using string formatting, and assigns them to three variables.
"""
import random

# Generate random floats
random_float1 = random.random()
random_float2 = random.random()
random_float3 = random.random()

# Convert the floats to strings
string1 = f"{random_float1:.6f}"
string2 = f"{random_float2:.6f}"
string3 = f"{random_float3:.6f}"

# Print the strings (optional, for verification)
print(string1)
print(string2)
print(string3)