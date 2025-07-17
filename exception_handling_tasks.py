"""
Exception Handling in python
"""

"""
 Handle Division by Zero
"""

def divide(a: int, b: int) -> None:
    try:
        _ = a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Done")
    finally:
        print("Exiting divide method")

divide(10, 0)
divide(20, 30)

"""
Use Multiple except Blocks
"""

def parse_input(input_str: str) -> None:
    try:
        _ = int(input_str)
    except ValueError:
        print("Value not supported to parse")
    except TypeError:
        print("Type not supported to parse")
    else:
        print("Parsed value is:", _)

parse_input("abc")
parse_input(None)
parse_input("123")

"""
Use else with try
"""

def check_file(file_name: str) -> None:
    try:
        f = open(file_name, 'r')
        file_data = f.read()
    except FileNotFoundError:
        print("No file found")
    else:
        print("File opened")
        print(file_data)
        f.close()

check_file("/home/saivarma/Downloads/params.csv")

"""
Use finally for Cleanup
"""

def safe_read(file_name: str) -> None:
    try:
        f = open(file_name)
        print(f.readline())
    except Exception as e:
        print("Error while reading the file", e)
    finally:
        try:
            f.close()
        except:
            print("File was never opened")

safe_read("/home/saivarma/Downloads/params.csv")


"""
raise Custom Exceptions
"""

def is_valid_age(age: int) -> bool:
    if age <= 0:
        raise ValueError('Age must be greater than 0')
    return True

# is_valid_age(0)
print(is_valid_age(20))

"""
assert Statement
"""

def is_valid_age_assert(age: int) -> bool:
    assert age > 0 and isinstance(age, int), "Age must be greater than 0 and valid number"
    return True

# print(is_valid_age_assert(0))
print(is_valid_age_assert(20))

