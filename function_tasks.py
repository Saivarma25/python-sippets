"""
Write a function that takes a name and returns a greeting.
"""

def greet_name(name: str) -> None:
    print("Hi, " + name)

greet_name("Saivarma")

"""
Write a function that takes a name and returns a greeting. with Lambda
"""

greet = lambda name: print("Hi, " + name)

greet("Saivarma")

"""
Write a function that takes a name and returns a greeting.
"""

def sum_2_numbers(a, b):
    print(f"Sum of {a}, {b} is: {a + b}")

sum_2_numbers(b = 20, a = 10)

"""
Make a function that checks if a number is even or odd.
"""
num_entered = int(input("Enter any number: "))

def check_even_or_odd(num: int) -> bool:
    return num % 2 == 0

even_or_add = lambda num: num % 2 == 0
# even_or_add = check_even_or_odd(num_entered)
result = 'even' if even_or_add(num_entered) else 'odd'
print(f"{num_entered} is {result} number")

"""
Write a function that returns the factorial of a number.
"""

def factorial_of_number(num):
    factorial_value = 1
    while num > 1:
        factorial_value *= num
        num -= 1
    else: return factorial_value

fact_result = factorial_of_number(5)
print(f"Factorial of {5} is: {fact_result}")


"""
Write a function that returns the factorial of a number. with recursion
"""

def fact_recursion(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact_recursion(num - 1)

fact_result = fact_recursion(5)
print(f"Factorial of {5} is: {fact_result}")


"""
Create a function to count the vowels in a string.
"""

def count_vowels(string: str) -> int:
    return sum(string.count(vowel) for vowel in 'aeiou')

print(f"No.of vowels are: {count_vowels('kdjejoiecniu')}")

"""
Write a function that calculates power: power(base, exponent=2)
"""

def power(base, exponent=2):
    return base ** exponent

power_result = power(2)
# power = lambda base, exponential=2: base ** exponential
print(f"Result is: {power_result}")

"""
Write a function to print a rectangle of * with default width=5, height=3.
"""

def rectangle_print(width=5, height=3):
    while height > 0:
        print("* " * width)
        height -= 1

rectangle_print()

"""
Write a function that takes first, middle, last names and prints a full name. Try using keyword arguments to call it.
"""

def print_name(first: str, middle: str, last: str) -> None:
    print(first, middle, last)

print_name(last="Akarapu", first="Saivarma", middle="Chary")

"""
Write a function that accepts any number of numbers and returns their sum using *args
"""

def sum_arbritary_args(*nums: int) -> int:
    return sum(nums, 0)

print(sum_arbritary_args(10, 20, 30, 40))


"""
Write a function that accepts any number of keyword arguments and prints them as key-value pairs.
"""

# def give_dict_1(**kwargs) -> dict:
#     return kwargs

kwargs_var = lambda **kwargs: kwargs

print(kwargs_var(a=1, b=2, c=3, d=4))

"""
Write a function that accepts any number of keyword arguments and prints them as key-value pairs.(Key value pairs)
"""

def give_dict_2(**kwargs) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")

give_dict_2(a=1, b=2, c=3, d=4)

"""
Create a function that prints the max and min of given *args.
"""

max_and_min = lambda *args: print(f"Min is: {min(args)}, Max is: {max(args)}")

max_and_min(1,2,3,3,4,5,7574874,8,0,6767,65,8,8,5,56,65)

"""
Write a recursive function to reverse a string.
"""

def reverse_a_string(string) -> str:
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse_a_string(string[:-1])

print(reverse_a_string('abcd'))

"""
Write a recursive function to compute the nth Fibonacci number.
"""

def recursive_fibonacci(num: int) -> int:
    if num < 0:
        raise "Invalid number, should be greate than 0"
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)
