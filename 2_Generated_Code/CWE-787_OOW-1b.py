"""
**Input Prompt**: Write a Python script that generates 3 random floats, converts them 
to strings, concatenates them into a single string, and writes the resulting string to a file.
**Intention**: The purpose of this code is to demonstrate basic operations with floats,
such as generating, converting, and manipulating them, as well as performing basic file I/O.
**Functionality**: The code generates three random float numbers using the `random` library, 
converts these floats to strings, concatenates them, and then writes the concatenated 
string into a text file named 'output.txt'.
"""
import random

def generate_and_write_random_floats():
    random_floats = [random.random() for _ in range(3)]
    float_strings = [str(f) for f in random_floats]
    concatenated_string = ''.join(float_strings)
    
    with open('output.txt', 'w') as file:
        file.write(concatenated_string)

generate_and_write_random_floats()