# Abstract class - Parent class that act as the primary and in sub classes, methods must be created to execute the operation
# Abstract method - Head methods that should contain only 'pass' so that whenever any ops are performed, it will be directed to the concerned class and method.

# Refer to the google document and youtube channel - 'code io Tamil' for more information.

from abc import ABC, abstractmethod                             # importing abstract method from abstract class

class Car(ABC):                                                 # Parent class which acts as Abstract Class
    @abstractmethod
    def MoveForward(self):                                      # Abstract method
        pass
    @abstractmethod
    def MoveBackward(self):
        pass
    @abstractmethod
    def SongPlay(self):
        pass

class Polo(Car):
    def MoveForward(self):
        print(f"The car is moving forward!")
    def MoveBackward(self):
        print (f"The car is moving backward!")
    def SongPlay(self):
        print(f"I am listening to Timeless by The Weeknd!")

class Virtus(Car):
    def MoveForward(self):
        print(f"The car is moving forward!")
    def MoveBackward(self):
        print (f"The car is moving backward!")
    def SongPlay(self):
        print(f"I am listening to New York Nagaram by AR Rahman!")

s1 = Virtus()
s1.SongPlay()