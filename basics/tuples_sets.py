# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Use a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

#Single value needs trailing comma
fruits3 = ('Apples') # if you only have one value you need a trailing comma, otherwise it only sees it as a string
print(fruits3, type(fruits3))
fruits4 = ('Apples',)
print(fruits4, type(fruits4))

# Get a value
print(fruits[1]) 

# In tuples you cannot change the values
# fruits[0] = 'Pears' # you get type error, tupe does not support item assignment

# Delete tuple
del fruits2

# Len of tuple
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set 
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if something is in a set
print ('Apples' in fruits_set)

# Add to set 
fruits_set.add('Grapes')
print(fruits_set)

# Add to set 
fruits_set.add('Apples')
print(fruits_set) # Will no give errors but will not add it 

# Remove
fruits_set.remove('Grapes')
print(fruits_set)

# clear set 
fruits_set.clear()
print(fruits_set) # gives empty set



