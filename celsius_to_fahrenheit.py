"""
1: Program to convert temperature from Celsius to Fahrenheit
"""

def convert_c_to_f():
    return celsius *  9/5 + 32

celsius = int(input("Enter Celsius: "))
print(f"{convert_c_to_f()}F")
