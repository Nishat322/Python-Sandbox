# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    #Constructor - function that runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        self.name = name # self is similar to this
        self.email = email
        self.age = age
    # Create method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Init user object
brad = User('Brad Travesay', 'brad@gmail.com', 37)

print(type(brad))

# Acess Property
print(brad.name)
# Acess Method
brad.has_birthday()
print(brad.greeting()) # methods are called with two parenthesis

# Extend class - you still have access to the object class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name # self is similar to this
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init Customer Obj
janet = Customer('Janet', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())
