# while loop

value = 1
while value <= 10:
    print(value)
    value += 1


value = 1
while value <= 10:      # Executes until the condition is true
    print(value)
    if value == 5:
        print("Time to break")
        break
    value += 1
else:
    print("This will not execute because we have a break")

value = 1
while value <= 10:
    value += 1  
    if value == 5:
        print("Continuing")
        continue
    print(value)
else:
    print("Prints when the while condition is not true")      

# for loop
# it executes over a sequence 
# 1. collection data like list, sets, tupes, dictionaries    
# 2. individual chars of a string

names = ["Sanjay", "Vandana", "Idhant"]

for n in names:     # we need to provide an iterable in for loop
    print(n)
else:
    print("Executed when for-loop condition is not satisfied")

for c in "Mississippi":
    print(c)    

print("Range starts at 0 by default")
for n in range(6):
    print(n)    

print("Range not starting at 0 but 9 is not included")
for n in range(4, 9):
    print(n)    

print("Range incremented by 8")
for n in range(4, 90, 8):
    print(n) 

actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + name + ".")

# Looping through dictionary
name_age_dict = {
    "John": 23,
    "Smith": 43,
    "Bella": 32,
    "Hermit": 64
}

print("Printing dictionary: ")
for key in name_age_dict:
    print(key, name_age_dict[key])


products = [
    {"name": "iPhone", "price": 1500},
    {"name": "iPad", "price": 1000},
    {"name": "Smartwatch", "price": 150},
    {"name": "iMac", "price": 3000},
    {"name": "iMini", "price": 2000}
]

for index, product in enumerate(products):     # Access the index of the element of the list
    print(f"{index}: {product["name"]}, {product["price"]}")

