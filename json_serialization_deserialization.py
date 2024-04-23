'''
Serialization means that converting the data into a stream so that it can be transmitted or saved easily.
Python Dictionary is a convenient data structure to serialize data.
When we serialize a dictionary we convert it into a JSON object.
'''

import json
import os

# Define a dictionary
data = {
	"name": "Sanjay",
	"gender": "Male",
	"city": "Brisbane"
}


serialized_json_data = json.dumps(data)		# dumps() Converts the dictionary to a json object
print(serialized_json_data)
print(type(serialized_json_data))		# This is a json string

# write the serialized data into a json file
with open("user_data.json", "w") as file:
	json.dump(serialized_json_data, file)

print("User data saved successfully")

# DESERIALIZE
#############

# Define a json object as string
json_string = '{"name": "Sanjay", "gender": "Male", "city": "Brisbane"}'

# loads() converts the string into a dictionary
data_dictionary = json.loads(json_string)
print(type(data_dictionary))	 # This will print dictionary
print(data_dictionary)


# Read JSON data from a file
if os.path.exists("user_data.json"):
	with open("user_data.json", "r") as file:
		data_read = json.load(file)

	print("JSON Data read from the file")
	print(data_read)
