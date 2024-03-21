# This is a custom module

# Import a module inside your own module
from random import choice

# Some constants/data
state = "Jharkhand"
capital = "Ranchi"

bird = "Peacock"

flower = "Rose"

sport = "Hockey"

# Functions

def randomfunfact():
    funfacts = [
        "Jharkhand has Chotanagpur Plateau",
        "Jharkhand is rich in mineral resources like iron, copper, coal, water, etc.",
        "Jharkhand has a city called Tata which is the home of India's biggest industrial house Tata",
        "Jharkhand has many beautiful dams and forests"
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()         # => this function is only called if jharkhand.py is the main file
                            # This may be a way to declare private functions inside a module. If you do not want to
                            # expose this function to outside world
    
#randomfunfact()