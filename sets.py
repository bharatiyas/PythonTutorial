nums1 = {1, 2, 3, 4}  # Creates a set, a collection of unique values. A list can have duplicates.

nums2 = set((1, 2, 3, 4, 5, 7, 8, 99))  # set() accepts a iterable like list or tuples

# Order of elements is not maintained in a set. So do not access elements using index.
# Sets are mutable just like lists

print(nums1)
print(nums2)
print(type(nums2))
print(len(nums2))

# No duplicates are allowed

nums3 = {1, 2, 2, 2, 3}
print(nums3) # prints {1, 2, 3}. Ignores repetitions

# True is a dupe of 1, False is a dupe of 0
# We can have different types of elemtns in the same set
nums3 = {1, True, 2, False, 3, 4, 0}
print(nums3)  # {False, 1, 2, 3, 4}  because of 1 True was ignored. Because of False 0 was ignored

# Check for a Value in set

print(2 in nums3)  # But you cannot refer to an element in the set with an index position

# Add a new element
nums3.add(46)
print(nums3)

nums3.update(nums2)
print(nums3)

# Removed an element from set. If the element is not present in the set then KeyError will be thrown
nums3.remove(1)

# To avoid the error use discard()
nums3.discard(100)

# To remove and return a randomly chosen element from a set
popped_out = nums3.pop()
print(popped_out)

# To delete all the elements from a set
nums3.clear()

nums3 = {1, 2, 2, 2, 3}

# Merge two sets
nums4 = nums1.union(nums3).union(nums2)
print(nums4)

nums3.intersection_update(nums1) # Keep only the duplicates
print(nums3)

nums2.symmetric_difference_update(nums1) # Keep everythings except the duplicates. 
                                         # This is opposite of intersection_update()
print(nums2)

s = {}  # Creates a dictionary, instead of set

# Create an empty
s = set()

# Operations on sets are similar to operations on mathematical sets. We can perform union, intersetion, of sets
set_a = {1, 2, 4, 5, 3}
set_b = {4, 5, 6, 7, 8}

# Union of two sets
print(set_a.union(set_b))
print(set_a | set_b)    # Union operator for sets

# Intersection of two sets
print(set_a.intersection(set_b))
print(set_a & set_b)

# Different of two sets
print(set_a.difference(set_b))  # Removes the common elements from set_a
print(set_a - set_b)