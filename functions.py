def say_hello():     # use def to define a function. All lower case and words separated by _
    print("Hello world!!")


# The arguments a, b are also called positional arguments because the position of the elements matters
def sum(num1, num2):
    return num1 + num2


# If you do not want to be bothered about the position of the arguments, in that case you can use Keyword arguments
def speed(distance, time):
    return distance/time


print(f"Speed is {speed(time=2, distance=100)}")       # Passing Keyword args


def sum_of_int(num1=0, num2=0):     # We provide default values of 0 to num1 and num2
    return num1 + num2


# If only on default value arg then you need to place the default args on right most
def divide_nums(num1, num2=1):
    return num1/num2


def add_multiple_items(*args):    # * for variable length positional arguments, when we do not know the number of args
    print(args)
    print(type(args))   # arguments are of type tuple
    result = 0
    for arg in args:
        result += arg
    return result


def multiple_named_items(**kwargs):     # ** for variable length key-word (named) arguments
    print(kwargs)
    print(type(kwargs))      # kwargs is of dictionary
    for key, value in kwargs.items():
        print(key + ": " + value)


multiple_named_items(name = "iphone", price = "700")
multiple_named_items(name = "ipad", price = "1000", description = "This is an ipad")

say_hello()
total = sum(2, 3)
print(total)

total = sum_of_int()
print(total)

multiple_items("Sanjay", "Vandana", 4)
multiple_named_items(first="Sanjay", second="Vandana", last=4)


# Return multiple values from a circle
def circle(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference


a, c = circle(10)
print(f"Area = {a}, Circumference = {c}")
