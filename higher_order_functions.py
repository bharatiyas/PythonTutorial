# Higher Order Functions (HOF) are functions which take 1 or more functions as arguments 
# or returns a function as its result (for example closures are HOF because they return a f())

# Example 1 : returns a function as its result

def funcBuilder(x):
    return lambda num: num + x      # funBuilder() is a higher order function because it returns a 
                                    # function

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(17))
print(addTwenty(15))

# Example 2 : Takes functions as arguments

numbers = [3, 7, 12, 18, 20, 29]

sqaured_nums = map(lambda num : num * num, numbers)   # map() is HOF which takes 2 params:
                                                      # 1. lambda f()
                                                      # 2. parameter on which the lambda f() will be 
                                                      #     applied to


print(list(sqaured_nums))

# Example 3 : filter()

lambda num : num % 2 !=0

odd_nums = filter(lambda num : num %2 != 0, numbers)
print(list(odd_nums))

# Example 4 : reduce()

from functools import reduce


total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)

###############################



names = ['Sanjay', 'Idhant', 'Bandana']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)