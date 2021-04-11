# If/ Else conditions are used to decide to do something based on something being true or false
x = 10
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y : 
    print(f'{x} is greater than {y}')

# If/else
if x > y : 
    print(f'{x} is greater than {y}')
else :
    print(f'{y} is greater than {x}')

# elif
if x > y : 
    print(f'{x} is greater than {y}')
elif x == 7: 
    print(f'{x} is equal to {y}')
else :
    print(f'{y} is greater than {x}')

# Nested if 
if x > 2 :
    if x <= 10 :
        print(f'{x} <= 10')

# Logical operators (and, or, not) - Used to combine conditional statements
if x > 2 and x <= 10 :
    print(f'{x} is <= 10')

if x > 2 or x <= 10 :
    print(f'{x} is <= 10')

if not(x == y) :
    print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1,2,3,4,5]
z = 3

if z in numbers:
    print(z in numbers)

if x not in numbers: 
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
b = 3
c = 3
if b is c:
    print(b is c) 

d = 4
if b is not d:
    print(b is not d)