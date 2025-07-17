import random
import time
"""
Positive, Negative, or Zero
"""

input_num = input('Enter any number:')
if input_num.lstrip('-').isnumeric():
    input_num = int(input_num)
    print("Positive number") if input_num > 0 else print("Negative number") if input_num < 0 else print("Zero")
else: print("Not a valid number : (")

"""
Even or Odd Checker
"""
input_num = input('Enter any number:')
if input_num.lstrip('-').isnumeric():
    input_num = int(input_num)
    print(f"{input_num} is an Even Number") if input_num % 2 == 0 else print(f"{input_num} is an Odd Number")
else:
    print("Please enter valid number")

"""
Even or Odd Checker final
"""
try:
    input_num = int(input("Enter any number:"))
    result = "Even" if input_num % 2 == 0 else "Odd"
    print(input_num, "is an", result, "number")
except ValueError:
    print("Invalid value")

"""
Age Group Classifier
"""
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Senior")

"""
Simple Calculator
"""
operator: str = input("Enter any operator: ")
value_1: int = int(input("Enter value 1: "))
value_2: int = int(input("Enter value 2: "))

match operator:
    case '+':
        print(value_1 + value_2)
    case '-':
        print(value_1 - value_2)
    case '*':
        print(value_1 * value_2)
    case '/':
        print(value_1 / value_2)
    case _:
        print("No matching operator")

"""
Password Validator
"""

actual_pwd = "saivarma"
entered_password = ""

while actual_pwd != entered_password:
    entered_password = input("Enter your password: ")
else:
    print("Passwords matched")

"""
Guess the Number
"""

random_number = random.randint(1, 10)
entered_number = 0

while random_number != entered_number:
    entered_number = int(input("Enter any random number"))
else:
    print("You guessed the number correctly")


"""
Sum Until Zero
"""

user_input = -1
total_sum = 0

while user_input != 0:
    user_input = int(input("Enter any number: "))
    total_sum += user_input
else:
    print(f"Total sum is {total_sum}")

"""
Multiplication Table
"""

number_for_mult_table = int(input("Enter any number: "))
till_num = 1

while till_num <= 10:
    print(number_for_mult_table, '*', till_num, '=', number_for_mult_table * till_num)
    till_num += 1
else:
    print(f"Multiplication table done for {till_num - 1} times")

"""
Countdown
"""

number_countdown = int(input("Enter a number for countdown: "))

while number_countdown >= 0:
    print(number_countdown)
    time.sleep(1)
    number_countdown -= 1

"""
Print First N Natural Numbers
"""

for i in range(1, number_for_mult_table + 1):
    print(i, end=" ")

"""
Factorial Calculator
"""

fact_result = 1
for n in range(number_for_mult_table, 0, -1):
    fact_result *= n
else:
    print(f"Factorial of {number_for_mult_table} is: {fact_result}")

"""
Sum of Squares
"""

sum_of_squares = 0

for i in range(1, number_for_mult_table + 1):
    sum_of_squares += i ** 2
else:
    print(f'Sum of squares of given n natural numbers is: {sum_of_squares}')


"""
Fibonacci Series
"""

first_num_fib = 0
second_num_fib = 1
new_num = 0

if number_for_mult_table < 2:
    print("Input should be greater than 2")
else:
    print(first_num_fib, second_num_fib, end=" ")
    for _ in range(number_for_mult_table - 2):
        new_num = first_num_fib + second_num_fib
        print(new_num, end=" ")
        first_num_fib = second_num_fib
        second_num_fib = new_num

"""
Count Vowels in a String
"""
input_str = input("Enter any string: ")
vowels_count = 0
vowel_string = 'aeiou'

for char in input_str.lower():
    if char in vowel_string:
        vowels_count += 1
else:
    print("Vowels in given string are: ", vowels_count)