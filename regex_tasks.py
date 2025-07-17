"""
RegEx tasks
"""
import re

"""
Check if string is email
"""

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

print(is_valid_email("saivarma@gmail.com"))
print(is_valid_email("saivarma.com"))

"""
Extract all numbers from a string
"""

text = "Order 5 pizzas, 3 burgers, and 1 coke"

numbers: list[str] = re.findall(r'\d+', text)
numbers: list[int] = [int(num) for num in numbers]

for num in numbers:
    print(num)

"""
Check if a string is valid PAN format (e.g., ABCDE1234F)
"""

def is_valid_pan(pan: str) -> bool:
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return re.fullmatch(pattern, pan) is not None

print(is_valid_pan("ABCDE1234M"))
print(is_valid_pan("AHGjg1234M"))

"""
Validate phone number (e.g., 10 digits, optional country code)
"""

def is_valid_phone(number: str) -> bool:
    pattern = r'^\d{10}$'
    return re.fullmatch(pattern, number) is not None

def is_valid_indian_phone(number: str) -> bool:
    pattern = r'^(?:\+91|91|0)?[6-9]\d{9}$'
    return re.fullmatch(pattern, number) is not None

print(is_valid_phone("9876543210"))
print(is_valid_phone("98765 43210"))
print(is_valid_phone("123456"))
print(is_valid_indian_phone("+919876543210"))
print(is_valid_indian_phone("5123456789"))

"""
Replace all vowels in a string with `*`
"""

text = "Saivarma is learning Python"
replaced = re.sub(r'[aeiouAEIOU]', '*', text)

print(replaced)

"""
Find the First Occurrence
"""

text = "This report was submitted on 25-06-2024 and approved on 30-06-2024."

match_obj = re.search(r'\b\d{2}-\d{2}-\d{4}\b', text)
print(match_obj.group())

"""
Given a paragraph, split it into sentences using ., !, or ? as delimiters.
"""

text = "Hello there! How are you doing? Let's learn regex. It's fun."

results = re.split(r'[.!?]\s', text)

print(results)
for result in results:
    print(result, end=" ")
