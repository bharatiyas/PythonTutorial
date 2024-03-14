# Tuples are like lists. But the data inside the tuples will NOT change. Also, the order of the data will NOT change

tuple1 = tuple(('Sanjay', 44, True))
print(tuple1)

tuple2 = ('Bharatiya', 3, 4.5, False, 3, 3, 4)
print(tuple2)
print(type(tuple2))

# Most of the things which apply to List are also applicable to Tuples, except they cannot be changed

newList = list(tuple2)
newList.append('Idhant')
tuple3 = tuple(newList) # When we assign a new value to a tuple then that is called packing a tuple

print(tuple3)

#  Unpack a tuple
(one, two, *rest) = tuple3 # rest will be assigned the 3rd and onwards values form tuple3
print(one)
print(two)
print(rest)

(one, *twoonwards, last) = tuple3   # unpacking in the middle
print(one)
print(*twoonwards)
print(last)

print(tuple2.count(4)) # count the number of occurrences of 4