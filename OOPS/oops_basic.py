
# This is the entire block of core parts on OOPS related to Class, methods and Object

class cricket:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def team(self):
        print("CSK")
    
    def add_two(self, x):
        return x + 2

c = cricket("Dhoni", 43)
print(c.add_two(c.age))


class cricket:                                  # Class is the blueprint for creating objects
    def __init__(self, name, age):              # __init__ is the constructor method and runs automatically when the object is created
        self.name = name
        self.age = age                          # Why should we use 'self' is because the object needs to access the data present in the method. If not, it won't know that you are referring to the object's own
    
    def team(self):                             # Method 2 - team()
        print("CSK")
    
    def add_two(self, x):                       # Method 3 - add_two(x)
        return x + 2

c = cricket("Dhoni", 43)                        # Object - c
print(c.add_two(c.age))                        # Calling a method and print the output