
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