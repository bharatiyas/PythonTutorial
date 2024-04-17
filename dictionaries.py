# dictionaries are used to store data in (Key, Value) pair
# key and value both can be a string or a number

people_id = {
    1: "Ford",
    2: "Walton",
    3: "Parker"
}

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# using dict function to create a dictionary
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band2))
print(len(band))

# Access elements in the dictionaries. If the key does not exist in the dictionary this will throw an error
print(band["vocals"])

# Obtain the value using get method. The advantage here is that if the key does not exist in the dictionary then it will
# return None instead of an error.
print(band.get("guitar"))

# List all keys
print(band2.keys())

# List all values
print(band2.values())

# List key/value pairs as tuples
print(band2.items())

# Check for key
print("guitar" in band)
print("Page" in band)
print("triangle" in band)

# Change values. Dictionaries (like List) are mutable.
# If the key already exists then it is updated otherwiese a new entry is added
band["vocals"] = "Coverdale"

# Merge two dictionaries. New dictionaries values are added to the older ones. Any existing keys are updated new values.
# New keys are added with new values.
band.update({"bass": "JPJ"})

print(band)

# Remove items
bass = band.pop("bass")  # pop returns the value which has been removed
print(bass)
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # removes the last element that was added and returs as a tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]  # Deletes a specific key
print(band)

band2.clear() # Clears out all the elements
print(band2)

del band2 # Deletes the dictionary altogether

# Copy dictionaries

band2 = band # Just creates a reference called band2. Both of them refer to the same dictionary

bandCopy1 = band.copy()
bandCopy1["drums"] = "Mridanga"
print(band)
print(bandCopy1)

bandCopy2 = dict(band)  # use the constructor to create a copy
bandCopy2["drums"] = "tabla"
print(bandCopy2)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band3 = {
    "member1": member1,
    "member2": member2
}

print(band3["member1"]["name"])


