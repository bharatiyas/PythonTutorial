# Generators are functions which return an iterable

def even_generator(x):
	for i in range(x):
		if i%2 == 0:
			# instead of return we use yield. When yield is encountered function execution is stopped and a generator
			# object is returned to the function calling this function
			# yield implies that this is not a regular function, instead it is a generator function
			yield i


print(list(even_generator(20)))
