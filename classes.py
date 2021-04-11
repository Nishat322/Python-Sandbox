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
