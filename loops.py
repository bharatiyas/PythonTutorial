# while loop

value = 1
while value <= 10:
    print(value)
    value += 1
else:
    print("Prints when the while condition is not true")

value = 1
while value <= 10:
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

for n in names:
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