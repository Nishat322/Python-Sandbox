# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#no semi-colons, variables do not need var, const, let 
x = 1             # casted as an int by default
y = 2.5           # float
name = 'John'     # str - string 
is_cool = True    # bool - for booleans you need a capital T or F, otherwise it'll be looked as a variable

#Multiple Assignment 
x, y, name, is_cool = (1, 2.5, 'John', True) #same code as above 

#Basic Math 
a = x + y

#Check Type
print(type(x))

# Casting
x = str(x)
y = int(y)
print(type(x))
print(type(y), y) # 2.5 => will go to 2 
z = float(y)
print(type(z),z) # 2 ==> will go to 2.0, will not go back to 2.5 because y is no going from int 2 to float 2.0 

print (x, y, name, is_cool, a)
