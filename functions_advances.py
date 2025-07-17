"""
Apply any function to each element of a list
"""

def apply_to_list(fn, data):
    """Method that takes any function and applies it on to a list"""
    return [fn(item) for item in data]

def square(n):
    return n * n

def double(n):
    return n + n

def negate(n):
    return -n

print(apply_to_list(square, [1, 2, 3, 4]))
print(apply_to_list(double, [1, 2, 3, 4]))
print(apply_to_list(negate, [1, 2, 3, 4]))

print(list(map(square, [1, 2, 3, 4])))
print(list(map(double, [1, 2, 3, 4])))
print(list(map(negate, [1, 2, 3, 4])))


"""
 Closure: return a function that raises numbers to the power n.
"""

def make_power_function(factor):
    def power_fn(number):
        return number ** factor
    return power_fn

square_pow = make_power_function(2)

print(square_pow(5))

"""
 Closure: return a function that raises numbers to the power n. With Lambda
"""

def make_power_function_lamda(factor):
    return lambda n: n ** factor

cube_lam = make_power_function_lamda(3)

print(cube_lam(5))

"""
Lambda + Map

Convert a list of strings to uppercase
Add 5 to each number in a list
Get lengths of each word in a list of strings
"""

print(list(map(lambda x: x.upper(), "abcd")))
print(list(map(lambda x: x + 5, [1, 2, 3, 4])))
print(list(map(lambda x: len(x), ['abcd', 'ef', 'ghi', 'jklmn'])))

# Without lamda
print(list(map(str.upper, "abcd")))
print(list(map(len, ['abcd', 'ef', 'ghi', 'jklmn'])))


"""
Decorator
"""

def uppercase_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_output
def greet(name):
    return f"hello {name}"

print(greet('Saivarma'))


"""
Decorator Advanced
"""

import time
from functools import wraps

def logger(fn):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{fn.__name__}' with args={args}, kwargs={kwargs}")
        return fn(*args, **kwargs)
    return wrapper

def timer(func):
    def timer_wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] '{func.__name__}' took {end-start:.6f} seconds")
        return result
    return timer_wrapper

@logger
@timer
def print_numbers(n):
    for i in range(n):
        print(i)

print_numbers(10)







