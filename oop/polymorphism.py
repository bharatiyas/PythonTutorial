# Polymorphism = poly + morph
# poly = many
# morph = forms

# Polymorphism also means overloading. For example + operator is overloaded, so it can add or concatenate depending
# upon what it is being used for. This is an example of operator polymorphism
print(1+2)
print("1" + "2")

# Functional Polymorphism. For example, len() is polymorphic
# Returns the length of string here
print(len("Hello World"))

list_1 = [1, 3, 54, 67, 23]
# Returns the length of a list
print(len(list_1))


# Method overriding in OOP
class Food:

	def type(self):
		print('Food')

	def natural(self):
		print("Is natural or cooked")


class Fruit(Food):

	# type method here overrides the type method of the super class
	def type(self):
		print('Fruit')

	def color(self):
		print("Fruit's color")


orange = Fruit()
# Interpreter decides if it needs to use the method from the parent class or child class
orange.type()
orange.natural()
orange.color()
