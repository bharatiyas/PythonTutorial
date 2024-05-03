# Outer class
class Car:

	def __init__(self, brand, steering_covering):
		self.brand = brand

		# The instance of the Inner class is creating while creating the instance of the Outer class
		self.steering_object = self.Steering(steering_covering)

	@staticmethod
	def drive():
		print("Drive")

	# Inner class
	class Steering:

		def __init__(self, covering):
			self.covering = covering

		@staticmethod
		def rotate():
			print("Rotate")

		def get_covering(self):
			print(f"Steering Covering is of type {self.covering}")


car = Car("Palisade", "Leather")
car.drive()
steering = car.steering_object
print(steering.rotate())
print(steering.get_covering())
