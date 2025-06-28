class Sample:
    GRAVITY = 9.8
    numPeople = 0

    def __init__ (self, name="Tim"):
        self.name = name
    
    def showPeople(self):
        print(self.numPeople)
    
    def incPeople(self):
        self.numPeople += 1

s1 = Sample()

s1.showPeople()
s1.incPeople()

Sample.numPeople = 4

s1.showPeople()

s2 = Sample()

print(s2.numPeople)