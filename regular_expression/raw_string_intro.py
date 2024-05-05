# Raw string - is a string which does not have special characters. Ex, "Hello World" is raw string, but
# "Hello \n World" is not a raw string because it has a special character \n

# We define a raw string when we prepend r to the string. In that case the special character is not special anymore.
# It becomes a normal character
print(r"Hello \n World")

# We need raw strings to define search patterns in Python
