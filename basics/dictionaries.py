# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# simialr to objects in javascript

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person, type(person))

# Create using a constructor
person2 = dict(first_name = 'Sarah', last_name = 'Williams')
print(person2, type(person2))

# Get value 
print(person['first_name'])
print(person.get('last_name')) # more common method

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items 
print(person.items())

# Copy dict 
person3 = person.copy()
person3['city'] = 'Boston'
print(person3) # similar to how a spread operator works in javascript

# Remove an item
del(person['age'])
print(person)
person.pop('phone')
print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person3))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[1]['name']) # get value of key name in the second list item