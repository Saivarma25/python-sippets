"""
JSON module tasks
"""

import json

x = dict(name="sv", id=1)

x_as_str = json.dumps(x)
print(f"{x_as_str} and it is of type {type(x_as_str)}")

"""
 Deserialize JSON string to Python object
"""

new_str: str = '{"name": "sv", "id": 1}'

new_str_as_json = json.loads(new_str)
print(new_str_as_json, type(new_str_as_json))

"""
Parse nested JSON
"""

json_string: str = '''
{
    "name": "Saivarma",
    "address": {
        "city": "Hyderabad",
        "state": "Telangana",
        "pin": 500001
    },
    "skills": ["Python", "Java", "SQL"]
}
'''

json_as_dict = json.loads(json_string)
print(json_as_dict)
print(json_as_dict["address"]["city"])


"""
Load a list of users
"""

json_data: str = '''
[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Saivarma", "age": 28}
]

'''

users = json.loads(json_data)

for user in users:
    print(user["name"])