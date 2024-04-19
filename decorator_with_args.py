def decorator(func):
	# To make the wrapper flexible so that it can be used to decorate functions with arguments and no arguments,
	# we will pass variable length positional arguments and variable length key-word args
	def wrapper(*args, **kwargs):
		print("Better decorator-wrapper up side")
		func(*args, **kwargs)
		print("Better decorator-wrapper down side")

	return wrapper


# Function with arguments
@decorator
def ice_cream(name):
	print(f"I love {name} ice-cream")


# Call function with parameters
ice_cream("Strawberry")


# Function without arguments
@decorator
def chocolate():
	print("I love chocolate.")


# Call function with no parameters
print("\n\n")
chocolate()
