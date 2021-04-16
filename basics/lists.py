# A List is a collection which is ordered and changeable. Allows duplicate members.

# Similar to arrays

# Create List
numbers = [1,2,3,4,5] # more common way to create lists
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers, numbers2)

# Get a value 
print(fruits[1])

#Get length of list
print(len(fruits))

# Append the list 
fruits.append('Mangos')
print('add to list at end', fruits)

# Remove from list
fruits.remove('Grapes')
print('remove', fruits)

# Insert into a specific position
fruits.insert(2, 'Strawberries')
print('insert at pos', fruits)

# Change value
fruits[0] = 'Blueberries'

# Remove from specific positions
fruits.pop(2)
print('remove from pos',fruits)

# Reverse list 
fruits.reverse
print('reverse', fruits)

# Sort alphabetically
fruits.sort()
print('sort', fruits)

# Reverse sort
fruits.sort(reverse = True)
print('reverse sort', fruits)