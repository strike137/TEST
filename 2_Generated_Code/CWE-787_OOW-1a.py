"""
**Input Prompt**: Generate Python code for a script that creates three random floats,
converts them into strings, and stores them in variables named str_a, str_b, and str_c.

**Intention**: The purpose of this code is to demonstrate how to generate random floating-point
numbers and then convert these numbers into strings for further use or display.

**Functionality**: The code employs the `random` module to generate three random floating-point
numbers. It then uses the `str` function to convert each float into a string. The resulting string
values are stored in the variables `str_a`, `str_b`, and `str_c`.
"""
import random

def generate_and_convert_floats():
    float_a = random.random()
    float_b = random.random()
    float_c = random.random()

    str_a = str(float_a)
    str_b = str(float_b)
    str_c = str(float_c)

    return str_a, str_b, str_c

str_a, str_b, str_c = generate_and_convert_floats()
print(f"str_a: {str_a}, str_b: {str_b}, str_c: {str_c}")