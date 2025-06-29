# Encapsulation - The first concept in OOPS which refers to the bundling of data (attributes) and methods (functions) that operate on that data within a single unit, typically a class.

# Getter - retrieve the value of a private attribute.
# Setter - set or modify the value of a private attribute.

class cricket():                                # Main or parent class
    def __init__(self, name, captain, place):
        self.name = name
        self.captain = captain
        self.__place = place                    # __place - Private variable


    def read_place(self):                       # Getter method - Method is developed to read the private variable outside class
        print(self.__place)
    
    def change_place(self, place):             # Setter method - Method is developed to change the private variable outside class
        self.__place = place


set1 = cricket("CSK", "MSD", "Chennai")

set1.read_place()                               # Reading private variable through read_place()

set1.change_place("Pune")                       # Changing private variable through change_place()

set1.read_place()