'''
Something which is used to decorate a function. They modify the behaviour of a function without adding/deleting lines
of code to/from the function.
'''


def chocolate():
	print("Chocolate")


# Decorator is also a function, we can name it anything we like. Then we pass a function parameter to the decorator, the
# function which we want to modify. In this
def decorator(func):
	# Create wrapper function within which you need to modify the behaviour of the passed in function
	def wrapper():
		print("Wrapper up side")
		func()
		print("Wrapper down side")

	return wrapper


# Pass the function you want to decorate
choc = decorator(chocolate)
choc()

