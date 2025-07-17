"""
PIP with some packages
PIP is a package manager for python
-> Can create packages globally or inside venv
-> pip install package_name
-> pip show package_name
-> pip list
-> pip uninstall package_name
"""

import requests

#  GET request

try:
    get_response: requests.models.Response = requests.get("http://localhost:1234/checkHealthBySV")
    print(get_response.status_code, get_response.text)
except requests.exceptions.ConnectionError:
    print("Connection not established")

# POST request

try:
    post_response = requests.post("http://localhost:1234/relayEvents", json={"id":1, "value": 1})
    print(post_response)
    print(post_response.json())
except requests.exceptions.ConnectionError:
    print("Connection not established")


"""
To send request params and headers both can be inside {}
(params=params, headers=headers)
"""
