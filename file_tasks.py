"""
Dealing with files
"""
from io import TextIOWrapper

"""
Read
"""

f: TextIOWrapper = open("file_to_read.txt")
print(f.read())
f.close()

"""
Read using "with", no need of manual file close when using with
"""

with open("file_to_read.txt") as f:
    # print(f.read()) read only first 10 characters like below
    print(f.read(10))

"""
Read line by line
"""

with open("file_to_read.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

"""
Read line by line with for loop
"""

with open("file_to_read.txt") as f:
    for x in f:
        print(x)

"""
Append to a file
"""

with open("file_to_read.txt", "a") as f:
    print(f.write("\nAdding some text from python"))

with open("file_to_read.txt") as f:
    print(f.read())

"""
Overwriting to a file
"""

with open("file_to_read.txt", 'w') as f:
    f.write('New data from python')
    f.write('\nOld data has been overridden with "w" command')

"""
Create a new file 'x', 'w', 'a' can create files but w and a has extra purposes
"""

f = open("file_by_py.txt", "x")

"""
Delete a file, to delete a file we need os module
"""
import os

os.remove("file_by_py.txt")

"""
Delete a file by checking if it exist
"""

if os.path.exists("file_to_read.txt"):
    os.remove("file_to_read.txt")
    print("File deleted successfully")
else:
    print("file does not exist")
