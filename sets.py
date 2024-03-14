nums1 = {1,2,3,4} # Creates a set

nums2 = set((1,2,3,4,5,7,8,99))

print(nums1)
print(nums2)
print(type(nums2))
print(len(nums2))

# No duplicates are allowed

nums3 = {1,2,2,2,3}
print(nums3) # prints {1, 2, 3}. Ignores repetitions

# True is a dupe of 1, False is a dupe of 0

nums3 = {1, True, 2, False, 3, 4, 0}
print(nums3) # {False, 1, 2, 3, 4}  because of 1 True was ignored. Because of False 0 was ignored

# Check for a Value

print(2 in nums3) # But you cannot refer to an element in the set with an index position

# Add a new element
nums3.add(46)
print(nums3)

nums3.update(nums2)
print(nums3)

# Merge two sets
nums4 = nums1.union(nums3).union(nums2)
print(nums4)

nums3.intersection_update(nums1) # Keep only the duplicates
print(nums3)

nums2.symmetric_difference_update(nums1) # Keep everythings except the duplicates. 
                                         # This is opposite of intersection_update()
print(nums2)