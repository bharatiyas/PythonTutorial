# String data type

## Literal assignment

firstName = 'Sanjay'
lastName = 'Bharatiya'

print(type(firstName))
print(type(firstName) == str)
print(isinstance(firstName, str))

## Using Constructor function

pizza = str("Chicken")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation

fullName = firstName + " " + lastName
print(fullName)

fullName += "!!"

print(fullName)

# Casting a number to a String
decade = str(1980)

print(isinstance(decade, str))
print(decade)

# Multiple lines
multiline = '''
Hey, How are you?  

I was just checking in.


All good?
'''

print(multiline)

# Escape special characters
sentence = 'I\'m back at work! \tHey!\n\nWhere\'s this at\\located?'

print(sentence)

# String Methods

print(firstName.lower())
print(firstName.upper())
print(firstName)

print(multiline.title()) # title() is like capitalize() in Dataweave
print(multiline.replace("good", "OK"))
print(len(multiline))
print("stripped - " + multiline.strip()) ## Remove whitespace

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# String index values
print(firstName[1])
print(firstName[-1]) # Last char in the string
print(firstName[1:-1]) # provide a range
print(firstName[0:2])
print(firstName[2:])

# Some methods that return boolean

print(firstName.startswith("S"))
print(firstName.endswith("Z"))

