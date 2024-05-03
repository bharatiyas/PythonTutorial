class Student:

	def __init__(self, name, age, roll_number):
		self.name = name
		self.age = age
		self.roll_number = roll_number


class School:

	def __init__(self, school_name):
		self.school_name =  school_name
		self.students = []

	def add_student(self, name, age, roll_number):
		student = Student(name, age, r_num)
		self.students.append(student)

	def display_students(self):
		for s in self.students:
			print(f"Name: {s.name}, age: {s.age}, roll number: {s.roll_number}")

	def edit_student(self, roll_nun_to_edit, new_name, new_age):
		filtered_student = list(filter(lambda s: s.roll_number == roll_nun_to_edit, self.students))
		if len(filtered_student) != 1:
			print("Invalid roll number to edit")
		else:
			filtered_student[0].name = new_name
			filtered_student[0].age = new_age

	def delete_student(self, roll_nun_to_delete):
		for s in self.students:
			if s.roll_number == roll_nun_to_delete:
				self.students.remove(s)
				print(f"Student with roll number: {s.roll_number}, found and deleted")
				break
		print(f"No student found with roll number {roll_nun_to_delete}")


pms = School("Pitts Modern School")


while True:
	print("Following are your choices: \n1) Add student \n2)Display list of students \n3) Edit student " +
		  "\n4)Delete Student \n5) Quit")
	choice = input("\nPlease enter your choice: ")

	if choice == "1":
		name = input("Enter name of the student: ")
		age = input("Enter age of the student: ")
		r_num = input("Enter roll number of the student: ")
		pms.add_student(name, age, r_num)
	elif choice == "2":
		pms.display_students()
	elif choice == "3":
		r_num = input("Enter roll number you want to edit: ")

		name = input("Enter new name of the student: ")
		age = input("Enter new age of the student: ")
		pms.edit_student(r_num, name, age)
	elif choice == "4":
		r_num = input("Enter roll number you want to delete: ")
		pms.delete_student(r_num)
	else:
		break
