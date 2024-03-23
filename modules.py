# modules are libraries that are based on common features like math, requests, etc
# modules contain functions or/and constants

# To see the list of modules visit:     https://docs.python.org/3/py-modindex.html

import sys
import random as rdm    # Using alias for imports

from math import pi
from enum import Enum   # enum is the module
import jharkhand #Import custom module
from closure_rps import rock_paper_scissors

print(pi)
print(rdm.choice("1234"))

#print(dir(sys))     # Print the list of functions in side the module

#for item in dir(rdm):
#    print(item)

print(__name__)     # this prints __main__ which is default name of the module which is running. Every module has it

# print(rdm.__name__)     # prints the name of the random module

print(jharkhand.capital)

jharkhand.randomfunfact()

print(jharkhand.__name__)   # prints the name of jharkhand module -> jharkhand

rock_paper_scissors()