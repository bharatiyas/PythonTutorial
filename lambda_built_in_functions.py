# map function

# Example 1
numbers = [1, 2, 3, 4, 6]

def square(x):
	return x * x

# Syntax is:  map(function_to_be_applied, iterable)
numbers_square = list(map(square, numbers))
print(numbers_square)

# Example 2
numbers_str = ["10", "72", "93", "42", "35"]
numbers = list(map(int, numbers_str))
print(numbers)

# Example 3
prices = [100, 200, 300, 400, 500]
# 5 % discount function
discounted_prices = list(map(lambda x: .95 * x, prices))
print(discounted_prices)

names = ["sanjay", "idhant", "vandana"]
capitalized_names = list(map(str.capitalize, names))
print(capitalized_names)

# filter
numbers = [23, 45, 66, 87, 90, 12, 24, 74, 98, 101, 203]
odd_nums = list(filter(lambda n: n % 2 != 0, numbers))
print(odd_nums)

names = ["John Doe", "Alice Smith", "Bob Ford", "Bruce Lee"]
initials = list(map(lambda name: "".join(map(lambda n: n[0], name.split())), names))
print(initials)


def is_prime_number(n):
	if n < 2:
		return True
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
		return True

print(is_prime_number(23))

def filter_prime_num(n):
	if n < 2:
		return True
	else:
		return len(list(filter(lambda i: n % i == 0, range(2, n)))) == 0

print(filter_prime_num(23))

# Filtering a list dictionary
students = [
	{"name": "Alice", "age": 18},
	{"name": "Maria", "age": 15},
	{"name": "Bob", "age": 20},
	{"name": "David", "age": 19},
	{"name": "Jake", "age": 16}
]

print(list(filter(lambda s: s["age"] > 18, students)))
