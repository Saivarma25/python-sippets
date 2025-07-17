"""

Create a base class Employee:

Attributes: name, emp_id

Method: get_details()

Create subclass Manager:

Additional attribute: department

Override get_details() to include department.
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass()
class Employee:
    name: str
    emp_id: int

    @staticmethod
    def get_details():
        print("parent function")

class Manager(Employee):
    def __init__(self, name: str, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def get_details(self):
        print(f"{self.name} with {self.emp_id} and {self.department}")

m = Manager('h', 1, 10)
m.get_details()


"""
Create class Person with __init__:

Create subclass Student and use super() to initialize inherited attributes.

Add additional attribute: student_id

Add a method show_details() that prints all attributes.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, student_id: str, name: str = 'sv', age: int = 20):
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        print(f"Student name {self.name} age: {self.age} id: {self.student_id}")

std = Student('101')
std.show_details()


"""
We can use @dataclass decorator as it creates __inti__ and other methods, extended classes init also can be taken care by it
"""

@dataclass
class PersonData:
    name: str
    age: int

@dataclass
class StudentData(PersonData):
    student_id: str

    def show_details(self):
        print(f"Student name is: {self.name} and age is: {self.age} with student id: {self.student_id}")

std_data = StudentData('Saivarma', 20, "15141A0502")
std_data.show_details()

"""
Class Animal with method make_sound()

Create Dog and Cat subclasses and override make_sound() method.

Create a function play_sound(animal) that takes any animal and calls make_sound() — shows polymorphism.
"""

class Animal:

    def make_sound(self) -> str:
        return 'Some sound'

class Dog(Animal):

    def make_sound(self) -> str:
        return 'Bow bow'

class Cat(Animal):

    def make_sound(self) -> str:
        return 'Meow Meow'

def play_sound(animal: Animal) -> str:
    return animal.make_sound()

print(play_sound(Dog()))
print(play_sound(Cat()))
print(play_sound(Animal()))

"""
Class Vehicle with __init__ initializing brand, model

Subclass Car adds seats attribute.

Use super() to initialize base attributes.

Add a method car_info() in Car.
"""

class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        return f"{self.brand} - {self.model}"

class Car(Vehicle):
    def __init__(self, brand: str, model: str, seats: int):
        super().__init__(brand, model)
        self.seats = seats

    def car_info(self):
        return super().vehicle_info() + f" with seats {self.seats}"

c = Car('Nissan', 'GTR', 2)
print(c.car_info())


"""
Create a base class Shape:

Method: area() (just print "Not implemented")

Create subclasses Circle, Square, Rectangle

Each should override area() to return actual area

Instantiate all and call area() in a loop
"""

@dataclass
class Shape:
    def area(self):
        print("Not Implemented")

@dataclass
class Circle(Shape):
    radius: int

    def area(self):
        print(f"Area of Circle is: {3.14159 * (self.radius ** 2)}")

@dataclass()
class Square(Shape):
    side: int

    def area(self):
        print(f"Area of Square is: {self.side ** 2}")

@dataclass()
class Rectangle(Shape):
    length: int
    width: int

    def area(self):
        print(f"Area of rectangle is: {self.length * self.width}")

circle = Circle(10)
square = Square(10)
rectangle = Rectangle(10, 10)

for obj in (circle, square, rectangle):
    obj.area()

"""
Create a Calculator class that:

Has one method add()

Try to define add(a, b) and add(a, b, c) separately (observe why it fails)

Then fix it using either default arguments or *args
"""

class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10, 20, 30, 40))

"""
Inheritance using abstract methods
"""

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        return "some sound"

class Dog(Animal):

    def make_sound(self):
        return "Bow Bow"

class Cat(Animal):

    def make_sound(self):
        return "Meow Meow"

print(Dog().make_sound())
print(Cat().make_sound())






