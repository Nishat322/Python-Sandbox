# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sarah', 'Susan']

# Simple for loop
for person in people:
    print(f'Current Person: {person}')

# Break (will print until it gets to Sarah (won't print Sarah))
for person in people: 
    if person == 'Sarah':
        break
    print(f'Current Person: {person}')

# Continue (will print everything but Sarah, will continue past Sarah)
for person in people: 
    if person == 'Sarah':
        continue
    print(f'Current Person: {person}')

# Range 
for i in range(len(people)):
    print(people[i])

# Custom range - will go from 0 to 10, will not go till 11
for i in range(0, 11):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
