"""
Arrays module in python
"""

import array as arr

signed_int_array = arr.array('i', [1, -2, 3, 4])

for item in signed_int_array:
    print(item)

unsigned_int_array = arr.array('I', [1, 2, 3, 4])

print(unsigned_int_array)

char_array = arr.array('u', ['a', 'b', 'c', 'd'])

print(char_array)

float_array = arr.array('f', [1.2, -2.4, 4.8])
print(float_array)

signed_long = arr.array('l', [1, -2, 3, -4])
print(signed_long)

unsigned_long = arr.array('L', [1, 2, 3, 4])
print(unsigned_long)

double_array = arr.array('d', [1.0, 2.0, 3.0, 4.0])
print(double_array)