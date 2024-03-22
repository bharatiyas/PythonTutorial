# Lambda function is a single expression which returns a value
# lambda is a key word in Python
# Lambda functions are anonymous functions

lambda num : num * num  # num * num is an expression which will square a number

cube = lambda num: num * num * num  # We can store a lambda in a variable

print(cube(3))      # print the cude of 3

lambda num: num + 2     # by default l labmda returns. We do not need to put an exclusive return statement
def addTwo(num): return  num + 2    # named function

print(addTwo(14))

lambda a, b: a + b
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