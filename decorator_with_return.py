def summer_discount_decorator(func):
	def wrapper(price):
		func(price)

		# Implement the changed functionality and return the function. In this case we are applying a 50% discount
		return func(price/2)
	return wrapper


@summer_discount_decorator
def total(price):
	return price


print(total(200))
