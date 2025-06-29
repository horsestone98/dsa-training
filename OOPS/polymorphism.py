# Explanation for polymorphism is provided in the Python google document.

# Method overloading

class Summation:
    def summ(self, *args):
        ans = 0
        for i in args:
            ans += i
        return ans
        
s1 = Summation()
print(s1.summ(1,2,3,4,5,6))



# Method overriding

class Father:
    def __init__(self):
        print("father constructor")
    
    def say_hello(self):
        print("Hello from father!")

class Child(Father):
    def __init__(self):
        print("child constructor")
    
    def say_hello(self, num):
        print("Hello from child!", num)


c = Child()
c.say_hello(2)

f = Father()
f.say_hello()