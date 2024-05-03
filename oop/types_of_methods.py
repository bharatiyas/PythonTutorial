# Instance method: Those methods which act on an instance variables of a specific class.
# Class method: Those methods which act upon a class variables
# Static method: They belong to the class but do not have access to instance variables and methods and to class variable

class Student:

	# Class variable
	category = "Student"

	# For class methods we use the decorator classmethod
	# For class methods we also pass cls instead of self
	@classmethod
	def get_category(cls):
		print(f"This is a class method of the class {cls.category}")

	def __init__(self, name, age):
		# instance variable
		self.name = name
		self.age = age

	# instance method as it acts upon an instance variable. We pass self to instance methods
	def get_student(self):
		print(f"Name of the student is: {self.name}")

	# Static method: Do not pass self or cls. You either leave it empty or just pass the parameters it requires
	# Static methods are like utility functions which do not depend on the class/state
	@staticmethod
	def age_difference(student_a, student_b):
		return student_a.age - student_b.age

idhant = Student("Idhant", 11)
idhant.get_student()

# Invoke a class method on the class (not on any object)
Student.get_category()

kunal = Student("Kunal", 12)
# Call the static method
age_diff = Student.age_difference(kunal, idhant)
print(age_diff)