import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(name):
    greeting = "hello, {}".format(name)
    return greeting


# inputname = input("Your Name? ")
print(greet("Dan"))

# r = requests.get('http://openedsauce.com')
# print(r.status_code)
