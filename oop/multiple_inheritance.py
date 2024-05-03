class A:

	def method_a(self):
		print("Method of class A")


class B:

	def method_b(self):
		print("Method of class B")


# C is inheriting multiple classes. It inherits from A and B
class C(A, B):

	def method_c(self):
		print("Method of class C")


# D is doing multi-level inheritance
class D(C):

	def method_d(self):
		print("Method of class d")

c_object = C()
c_object.method_a()
c_object.method_b()
c_object.method_c()

d_object = D()
d_object.method_a()
d_object.method_b()
d_object.method_c()
d_object.method_d()



