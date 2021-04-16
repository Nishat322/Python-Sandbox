# Python has functions for creating, reading, updating, and deleting files.

# Open a file 

myFile = open('myfile.txt', 'w') # will open the file and, set mode w for writing

# Get some info

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed) # did we close the file within the system
print('Opening Mode: ', myFile.mode)

#Wrtie to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file after closing
myFile = open('myfile.txt', 'a') # method to append, will no overwrite whatevers already in the file
myFile.write(' I also like PHP')
myFile.close()

# Read from a file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)