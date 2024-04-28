# List = Array. The order of the elements is maintained. It seems like it is a doubly linked list

users = ['Sanjay', 'Adam', 'Sai', 'Gavin']
#           0       1        2       3
#           -4      -3      -2      -1

print('Sanjay' in users)    # in operator to search for an element in a list
print('Roger' not in users)     # not in operator

data = ['Sanjay', 43, True]

emptyList = []

print('Sanjay' in users)
print(users[0])
print(users[-1])    # prints the last element in the array
print(users[-2])
print(users.index('Sai'))   # index() will return the index of the item
# print(users.index('Sairam'))        # Results in error because Sairam is not in the list
print(users[0:3])  # Does not include the value at position 3

print(users[1:])  # Includes the value at position 1

# Size/length of the list
print(len(users))

# Lists are mutable, means they can be changed

# append = Add an item to the end of the list
users.append('Chris')
print(users)

users += ['Nitin']
print(users)

users.extend(['Eshanee', 'Shalini']) # appends a list of items

print(users)

users += 'Roger' # Addess each charater of Roger as independent item in the list

print(users)

users.insert(0, 'Corey')  # Insert at a particular position

users[1] = 'Rakshit'    # Inserting a values using index
users[2:5] = ['Rijoy', 'Anusha', 'Linda']   # Inserting a range of values

users[2:2] = ['Kai', 'Rakshit'] # provide range of elements
print(users)

users.remove('Rakshit')  # Remove by value
print(users)

print(users.pop()) # Removes and returns the last element

del users[0]  # delete an element by position
print(users)

del data # Will delete the variable from the memory
# print(data)  ## Will now result in error

data = ['Sanjay', 43, True]
data.clear()    # Will remove all the elements from the arrary but the array is still present. It becomes an emplty list
print(data)

users.sort()
print(users)

users += ['charles']
users.sort(key = str.lower) # all the words are now sorted based on alphabetical order irrespective of case
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()  # reverses the order of elements in the list
print(nums)

nums.sort(reverse=True) # Modifies the list with new arrangement
print(nums)

print(sorted(nums, reverse=False)) # Global sorted() does NOT modify the original list

# Make a copy of the list
numscopy1 = nums.copy()
numscopy2 = list(nums)
numscopy3 = nums[1:3]  # copy from start to end index -1 only. this is also called list slicing.
numscopy4 = nums[:]     # copy the whole list
numscopy5 = nums[-3:]   # copy the elements from -3 to the end of the list
numscopy6 = nums[-3:0]  # this will not create any copy because we are mixing -ve and positive index

print(numscopy4)
print(type(nums))

# List slicing with [start:end:step]
alphabets = "abcdefghijklmnop"
print(alphabets[3:8:2])
print(alphabets[::2])
print(alphabets[::-1])		# Reverses the string/list

mylist = list([1, "Sanjay", True, 3.45, nums]) # Nesting a list inside a list. One list can have members of different datatypes
print(mylist)

list_a = [1, 2, 3]
list_b = [1, 2, 3]

print(list_a == list_b)   # this will print true because list_a and list_b have same elements in same order

# List concatenation
print(list_a + list_b)

# Repeat the elements (3 times in this case) in the list.
print(list_a * 3)

numbers = [1, 56, 87, 23, 19, 100, -53, 54, 12]
print((max(numbers)))
print((min(numbers)))

# you can have nested lists and there is no limitation on the number levels of nesting
nested_list = [1, 2, [3, 4], 5, 6, [7, 8, 9], 10]
print(nested_list[2][1])    # This will print 4

# join() to join all the elements of a list
apple = ['a', 'p', 'p', 'l', 'e']
print("".join(apple))
