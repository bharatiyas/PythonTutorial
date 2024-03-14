import math     # math module for mathematical operations

# integer

price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# float

gpa = 3.27
y = float(1.45)
print(type(y))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

 # Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))           # rounds to nearest integer
print(round(gpa, 1))        # rounds to nearest decimal

print(math.pi)
print(math.sqrt(70))
print(math.ceil(gpa))
print(math.floor(gpa))

zipcode = "10000"
zipcode_int = int(zipcode)
print(type(zipcode_int))
