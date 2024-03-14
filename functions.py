def say_hello():     # use def to define a function. All lower case and words separated by _
    print("Hello world!!")

def sum(num1, num2):
     return num1 + num2

def sum_of_int(num1=0,num2=0):     # We provide default values of 0 to num1 and num2
     return num1 + num2

def multiple_items(*args):    # * used when we do not know the number of arguments
     print(args)
     print(type(args))   # arguments are of type tuple

def multiple_named_items(**kwargs):     # ** for named arguments
     print(kwargs)
     print(type(kwargs))      # kwargs is of dictionary

say_hello()
total = sum(2, 3)
print(total)

total = sum_of_int()
print(total)

multiple_items("Sanjay", "Vandana", 4)
multiple_named_items(first = "Sanjay", second = "Vandana", last = 4)
 