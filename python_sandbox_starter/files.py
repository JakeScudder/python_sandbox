# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open("myfile.txt", "w")

# Get info
# print("Name: ", myFile.name)
# print("Is Closed: ", myFile.closed)
# print("Opening Mode: ", myFile.mode)

# Write to file
myFile.write("I love Python-- SIKE")
myFile.write(" and JavaScript")
myFile.close()

# Append to file

myFile = open("myfile.txt", "a")
myFile.write(" . YAYAYAYAYA")
myFile.close()

# Read from file
# myFile = open("myfile.txt", "r+")
# text = myFile.read(111)
# print(text)

# Re-Write
myFile = open("myfile.txt", "w")
myFile.write("Begin again, FRESH")
myFile.close()

# and then read
myFile = open("myfile.txt", "r+")
text = myFile.read(111)
print(text)
