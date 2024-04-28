# Lambda function is a single expression which returns a value
# lambda is a key word in Python
# Lambda functions are anonymous functions, so you cannot call them anywhere else.

# Normal function
def square(x):
    return x ** 2   # This function has only one line of code


print(square(4))

# We can write the same code using lambda to calculate the square. We do not give any name to lambda and write the code
# on the same line. We do not need to return the value, it's implicit return.
# We enclose the lambda within parenthesis because it does not have any name so, we need to call it here itself by
# passing an argument, as in this case 7 is the argument passed.
sqaure_of_7 = (lambda num: num ** 2)(7)
print(f"sqaure_of_7 = {sqaure_of_7}")

cube = lambda num: num * num * num  # We can store a lambda in a variable

print(cube(3))      # print the cude of 3

lambda num: num + 2     # by default l labmda returns. We do not need to put an exclusive return statement
def addTwo(num): return  num + 2    # named function

print(addTwo(14))

sum_of_2_nums = (lambda a, b: a + b)(2, 3)

# Using Keyword arguments
sum_of_2_numbers = (lambda a, b: a + b)(b=2, a=3)

# Using default values for parameters
sum_of_2_default_args = (lambda a=0, b=0: a + b)(b=2)

def sum(a, b): return a + b        # Two parameters for the lambda

print(sum(12, 2))

###########################################

# Generally used for quick function which may not be used in anyother place

# funcBuilder() helps in building other functions
def funcBuilder(x):
    return lambda num: num + x      # returns lambda function (similar to what is done closures)

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(17))
print(addTwenty(15))

