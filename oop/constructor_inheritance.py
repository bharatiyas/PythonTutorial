class Parent:

	def __init__(self):
		#
		print("Parent class constructor called")
		self.balance = 500000

	def display_balance(self):
		print(f"Parent's balance is: {self.balance}")


class Child1(Parent):
	pass
	# We are not defining any constructor for the child, therefore, Parent class constructor will be automatically
	# called when creating a child instance. This is called Constructor Inheritance


class Child2(Parent):

	def __init__(self):
		# Since we have created a child class constructor hence, we need to exclusively call the super class constructor
		# otherwise this Grandchild will not inherit the properties of the Parent
		super().__init__()
		print("Creating Child2 Object")


class Child3(Parent):

	def __init__(self):
		# If we do not call super constructor then balance would not be initialized for this child class. Therefore, we
		# exclusively need to assign balance here.
		# This is constructor overriding
		print("Creating Child3 Object")
		# If we do not assign balance here and try to access it, we will get an error
		self.balance = 20000


# When we create the instance of the Child, even though we do not have any constructor for the Child class, the
# constructor of the Parent class is called
child1_obj = Child1()
child1_obj.display_balance()

child2_obj = Child2()
child2_obj.display_balance()

child3_obj = Child3()
child3_obj.display_balance()
