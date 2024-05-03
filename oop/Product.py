class Product:

	# Class properties - These are not going to vary for each object we create. For example, we are selling 200 types
	# of product. These are like static variables in Java

	quantity = 200

	# Instance properties - These properties are specific to each object
	# We use a constructor to initialize the instance properties.
	# Constructor = __init__(self)	This is the signature of a constructor.

	# All the functions in python starting with __ are callback functions, meaning we do not call them instead they are
	# called by the interpreter.

	# init mean initializing the object we are creating. And self (= this in Java) is the reference to the object which
	# we are initializing.

	def __init__(self, name, price):		# Constructor with two positional arguments and are called object properties
											# They can be of any data type
		self.name = name		# this.name = name 		in Java
		self.price = price		# this.price = price 	in Java

	# Function within a class is called Method. Methods have access to class and object properties
	# We need to provide a reference to self so that this method can access the object properties of the object on which
	# it is being called.
	def summer_discount(self, discount_percent):
		return (100 - discount_percent)/100 * self.price


# Create an instance/object of the class. This will invoke the __init__ function mentioned above
p1 = Product("Phone", 300)
print(p1.quantity)

print("Discounted Price = ", p1.summer_discount(5))


class ChildProduct(Product):
	# If we do not write a code here this will throw an error. so, if we want to leave it empty we just write pass
	pass


child_prod = ChildProduct("Enjoy", 500)
print(child_prod.summer_discount(15))


class DigitalProduct(Product):

	def __init__(self, link):
		self.link = link

	def get_link(self):
		self.link = input("Enter product link")

	def put_link(self):
		print(self.link)



