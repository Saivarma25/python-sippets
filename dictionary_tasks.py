import string

"""
Group Words by Their First Letter
"""

words = ['apple', 'banana', 'apricot', 'blueberry']

key_set = set()
result_dict = dict()
for x in words:
    if x[0] not in key_set:
        key_set.add(x[0])

for y in key_set:
    result_dict[y] = [item for item in words if item.lower().startswith(y.lower())]

print(result_dict)

"""
Invert a Dictionary
"""

d = {'a': 1, 'b': 2, 'c': 1}
item_set = set()

result_dict = {}

for y in d:
    if d[y] in result_dict:
        result_dict[d[y]].append(y)
    else:
        result_dict[d[y]] = [y]

print(result_dict)

"""
Sort Dictionary by Value (Asc & Desc)
"""

data = {'apple': 3, 'banana': 1, 'cherry': 2}

value_set = list(data.items())
value_set.sort(key=lambda x_var: x_var[1])

print(dict(value_set))

"""
Sort Dictionary by Value (Asc & Desc) final
"""

data = {'apple': 3, 'banana': 1, 'cherry': 2}
result_dict = sorted(data.items(), key=lambda x_var: x_var[1])
print(dict(result_dict))

"""
Merge Two Dicts with Conflict Resolution
"""
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

result_dict = {}

for key, value in a.items():
    if key in b:
        result_dict.update({key: [value, b[key]]})
        del b[key]
    else:
        result_dict.update({key: value})

result_dict.update(b)

print(result_dict)

"""
Merge Two Dicts with Conflict Resolution
"""
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

result_dict = {}

for key in set(a).union(set(b)):
    if key in a and key in b:
        result_dict[key] = [a[key], b[key]]
    elif key in a:
        result_dict[key] = a[key]
    elif key in b:
        result_dict[key] = b[key]

print(result_dict)

"""
Count Word Frequency in a String (Ignore Case, Ignore Punctuation)
"""

text = "Hello hello! This is a test. This test is easy."

str_without_punctuation = text.translate(str.maketrans('', '', string.punctuation)).lower()

print(str_without_punctuation)

words = str_without_punctuation.split()
print(words)

result_dict = {}

for x in words:
    if x in result_dict:
        result_dict[x] += 1
    else:
        result_dict[x] = 1

print(result_dict)