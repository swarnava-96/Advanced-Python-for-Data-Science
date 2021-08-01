# Getting started with Oops
# A class can be considered as a real world objects that has attributes and functions

# Bad way of defining a class -- Creating an empty class
class car():
    pass

## Instantiating from the class
car1 = car()

car1

car1.windows = 5
car1.doors = 4

print(car1.windows)

## Creating another instance
car2 = car()

car2.windows = 3
car2.doors = 2

print(car2.doors)

car2.enginetype = "Petrol"
print(car2.enginetype)

# Now this is a bad way like if we dont fix the number of attributes the developer can create as many attributes as he likes.

# Proper way of defining a class--using a constructor
class car():
    def __init__(self, window, door, enginetype):
        self.windows = window
        self.doors = door
        self.enginetype = enginetype

# Here the self parameter is referencing the object car1
car1 = car(4, 5, 'Petrol')

# Lets create another such instance--Here the self parameter is referencing the object car2
car2 = car(3, 4, 'Disel')

print(car1.windows)
print(car2.enginetype)

# Lets define another class
class car():
    def __init__(self, window, door, enginetype):
        self.windows = window
        self.doors = door
        self.enginetype = enginetype
    def self_driving(self):
        return "This is a {} car".format(self.enginetype)

# Lets check
car1 = car(4, 5, "Petrol")
print(car1.self_driving())

