users = ['Sanjay', 'Adam', 'Sai', 'Gavin']

data = ['Sanjay', 43, True]

emptyList = []

print('Sanjay' in users)
print(users[0])
print(users[-1])
print(users[-2])
print(users.index('Sai'))
print(users[0:3]) # Does not include the value at position 3

print(users[1:]) # Includes the value at position 1

print(len(users))

users.append('Chris')
print(users)

users += ['Nitin']
print(users)

users.extend(['Eshanee', 'Shalini']) # appends a list of items

print(users)

users += 'Roger' # Addess each charater of Roger as independent item in the list

print(users)

users.insert(0, 'Corey') # Insert at a particular position

users[2:2] = ['Kai', 'Rakshit'] # provide range of elements
print(users)

users.remove('Rakshit') # Remove by value
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
numscopy3 = nums[1:3] # copy from start to end index only
numscopy4 = nums[:]

print(numscopy4)
print(type(nums))

mylist = list([1, "Sanjay", True, 3.45, nums]) # Nesting a list inside a list. One list can have members of different datatypes
print(mylist)