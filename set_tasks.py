"""
Find Common Elements Across Multiple Lists
"""
from os.path import commonpath

from tuple_tasks import duplicates

a = [1, 2, 3]
b = [2, 3, 4]
c = [2, 3, 5]

seen = set()

for x in a:
    if x in b and x in c:
        seen.add(x)

print(seen)

"""
Find Common Elements Across Multiple Lists final
"""
a = [1, 2, 3]
b = [2, 3, 4]
c = [2, 3, 5]

a, b, c = set(a), set(b), set(c)
# common = a.intersection(b, c)
common = a & b & c
print(common)

"""
Find Elements Unique to Only One List
"""
a = [1, 2, 3]
b = [3, 4, 5]

# common = set(a).symmetric_difference(set(b))
common = set(a) ^ set(b)
print(common)

"""
Remove All Vowels From a String Using Sets
"""

text = "beautiful"
vowels = set('aeiou')

result_str = ""

for x in text:
    if x not in vowels:
        result_str += x

print(result_str)

"""
Remove All Vowels From a String Using Sets final
"""

text = "beautiful"

result_str = "".join([c for c in text if c not in 'aeiou'])
print(result_str)

"""
Find Duplicate Elements in a List Using Set
"""
data = [1, 2, 3, 2, 1, 4]

seen = set()
duplicates = set()

for x in data:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(duplicates)


