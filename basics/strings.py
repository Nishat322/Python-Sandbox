# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate - insert variable into the string
# print('Hello, my name is ' + name + 'and I am ' + age) #error because you cannot concatenate a int, only string type
print('Hello, my name is ' + name + 'and I am ' + str(age))

# String Formatting
#   - Arguments by position
print('My name is {name} and I am {age}'.format(name = name, age = age))

#   - F-strings (only available to python version 3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitalize string
print('Capitalize: ', s.capitalize())

# Make all uppercase
print('Upper all cases: ', s.upper())

# Make all lower
print('Lower all cases: ', s.lower())

# Swap case
print('Swap cases: ', s.swapcase())

# Get length
print('find length, can be used an any data type: ', len(s))

# Replace
print('replace: ', s.replace('world', 'everyone'))

# Count
sub = 'h'
print('count the number of ...: ', s.count(sub))

# Starts with
print('check what it starts with, return true: ', s.startswith('hello'))

# Ends with
print('check what it ends with return false: ', s.endswith('d'))

# Split into a list
print('take string and turn into list (array): ', s.split())

# Find position
print('find the pos of the character: ', s.find('r'))

# Is all alphanumeric
print('return true or false is all characters alphanumeric?: ', s.isalnum()) # false because of the space inbetween the words

# Is all alphabetic
print('return true or false is all characters alphabetic?: ', s.isalpha()) # false because of the space inbetween the words

# Is all numeric
print('return true or false is all character numeric?: ', s.isnumeric())
