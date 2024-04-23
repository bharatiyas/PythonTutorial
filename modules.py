'''
modules are files that contain multiple functions or/and constants
modules are libraries that are based on common features like math, requests, etc
There are two types of modules:
	1. Built-in modules
	2. Custom modules
To see the list of modules visit:     https://docs.python.org/3/py-modindex.html
'''

import sys
import random as rdm    # Using alias for imports

from math import pi, floor		# Import multiple functions by using ,
import datetime
from enum import Enum   # enum is the module
import jharkhand  # Import custom module
# from closure_rps import rock_paper_scissors

print(pi)
print(rdm.choice("1234"))

# Print the list of functions in side the module
# print(dir(sys))

# for item in dir(rdm):
# print(item)

print(__name__)     # this prints __main__ which is default name of the module which is running. Every module has it

# print(rdm.__name__)     # prints the name of the random module

print(jharkhand.capital)

jharkhand.randomfunfact()

print(jharkhand.__name__)   # prints the name of jharkhand module -> jharkhand

print(floor(223.12))

# datetime is the module, date is a class inside datetime and today is the method
# functions defined inside a class are called methods
today = datetime.date.today()

#rock_paper_scissors()
