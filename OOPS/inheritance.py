# Inhertance - Passing the information from parent class to other sub classes to perform other set of operation which are not present in the main or parent class.

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and am {self.age} years old")
    def speak(self):
        print(f"I do not speak in the language you guys do")

class Doggy(Pet):
    def __init__(self, name, age, sound):
        super().__init__(name, age)     # super() - This operation is performed to call the values from Parent class
        self.sound = sound
    def voice(self):
        print(f"I am {self.name}, {self.age} years old and I {self.sound}")

p = Pet("Shadow", 4)
p.show()
d = Doggy("Shadow", 4, "bark")
d.voice()