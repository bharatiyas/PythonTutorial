import os   # Needed for write mode #2

#  RAWX  #
##########

# r = Read
# a = Append
# w = write
# x = Create

# Read - error if it does not exist

f = open("names.txt", "r")      # r - read the file (default value)

# f = open("names.txt", "rt")      # t - text file (default value),   b  - binary file

#  print(f.read())      # Read the file
print(f.read(5))    # Read first 5 chars of the file

# print(f.readline()) # Read a line from the file and then moved the file pointer to the next line. We read lines 1 by 1
# print(f.readlines())  # Reads multiple lines and returns them as a list of string

for line in f:      # Loop through the lines of the file
    print(line)

try:
    with open("file_does_not_exist.txt") as fdne:
        fdne.read()
except FileNotFoundError:
    print("File does not exist")
except:
    print("Error while operaing the file")
# when you get here, the fdne will be closed automatically.

# Append - creates a file if it does not exist
    
fa = open("names.txt", "a")    
fa.write("\nShubhankar")
fa.close()

try:
    # with is like a loop. When we use with to open a file, the file will be automatically closed by Python. We do
    # NOT exclusively close the file
    with open("names.txt") as fdne:
        print(fdne.read())
except FileNotFoundError:
    print("File does not exist")


# Write (Overwrite) - 2 modes
    
# 1. Opens a file for writing, created a file if it does not exist
fw = open("context.txt", "w")    
fw.write("I deleted all of the content of the file")
fw.close()

# 2. Create the specified file, but returns an error if the file exists
if not os.path.exists("not_exist.txt"):
    fne = open("not_exist.txt", "x")
    fne.close()

# Delete a file
# Avoid an error if the file does not exist
    
if os.path.exists("not_exist.txt"):
    os.remove("not_exist.txt")
else:
    print("File you wish to delete does not exist")



f.close()       # Everytime we open the file we should close the file so that changes are saved