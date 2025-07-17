"""
Using @dataclasses tp create a class better

this decorator will give __init__, __repr__ and __eq__ methods automatically
"""
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

    def describe(self):
        print(f"{self.title} was authored by {self.author}, pages: {self.pages} pages")

book = Book('Maths', 'SV', 100)
book.describe()
print(book.__repr__())
print(book.__str__())

"""
Create a Book class with attributes:

title, author, pages

Add a method describe() that prints all details.
"""

class Book:
    title: str
    author: str
    pages: int

    def describe(self):
        print(f"{self.title} was authored by {self.author} and has {self.pages} pages")

book = Book()
book.title = 'Maths'
book.author = 'SV'
book.pages = 100

book.describe()


"""
Same task using init
"""

class BookWithInit:
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.pages = page

    def describe(self):
        return f"{self.title} was authored by {self.author} which has {self.pages} pages"

print(BookWithInit('Maths', 'SV', 100).describe())

"""
Create a BankAccount class:

Attributes: account_holder, balance (default = 0)

Methods: deposit(), withdraw(), show_balance()

Use __init__ and object creation.
"""

class BankAccount:
    def __init__(self, account_holder: str, balance: int = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

    def show_balance(self):
        return f"{self.account_holder}'s balance is {self.balance}"

account1 = BankAccount('Sai', 1000)
account2 = BankAccount('Varma')

account1.deposit(1000)
print(account1.show_balance())

account1.withdraw(500)
print(account1.show_balance())

account2.deposit(1000)
print(account2.show_balance())

account2.withdraw(500)
print(account2.show_balance())


'''
Build a TemperatureConverter class with:

Method to_fahrenheit(celsius) and to_celsius(fahrenheit)
'''

class TemperatureConverter:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

print(TemperatureConverter.to_fahrenheit(20))
print(TemperatureConverter.to_celsius(10))
