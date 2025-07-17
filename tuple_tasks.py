# Mini programs on tuples
#

"""
Swap two variables without a temp variable
"""

a, b = 5, 10

tuple_var = (a, b)

b, a = tuple_var
print(a, b)

"""
Swap two variables without a temp variable final
"""
a, b = 5, 10
a, b = b, a
print(a, b)

"""
Sort a list of tuples by second element
"""
def sort_function(n):
    return n[1]

items = [(1, 3), (2, 1), (4, 2)]

items.sort(key = sort_function)

print(items)

"""
Sort a list of tuples by second element final
"""
items = [(1, 3), (2, 1), (4, 2)]

items.sort(key=lambda x: x[1])

print(items)

"""
Find duplicates in a list of tuples
"""
data = [(1, 2), (3, 4), (1, 2)]

result = [data[x] for x in range(len(data)) if data[x + 1:].count(data[x]) >= 1]

print(result)

"""
Find duplicates in a list of tuples final
"""
data = [(1, 2), (3, 4), (1, 2)]

seen = set()
duplicates = set()

for item in data:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(list(duplicates))

"""
Unpack and Repack
"""

point = (3, 5)

point = (point[1], point[0])
print(point)

"""
Unpack and Repack final
"""

point = (3, 5)
point = tuple(reversed(point))
print(point)