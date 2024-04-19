# Better way of decorating
# Put the decorator before the function being decorated


def decorator(func):
	# Create wrapper function within which you need to modify the behaviour of the passed in function
	def wrapper():
		print("Better decorator-wrapper up side")
		func()
		print("Better decorator-wrapper down side")

	return wrapper


@decorator
def ice_cream():
	print("I love ice-cream")


# The decorated functionality will be called
ice_cream()


# Same decorator can be used for decorating multiple functions
@decorator
def chocolate():
	print("I love chocolate.")


print("\n\n")
chocolate()
