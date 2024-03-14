# dictionaries are used to store data in (Key, Value) pair

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band2))
print(len(band))

# Access elements in the dictionaries
print(band["vocals"])

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

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass")) # pop returns the value which has been removed
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # removes the last element that was added and returs as a tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"] # Deletes a specific key
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

bandCopy2 = dict(band) # use the constructor to create a copy
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


