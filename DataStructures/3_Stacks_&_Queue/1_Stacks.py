# 1. Creating a stack

class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
class Stack():
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        return new_node
    
    def pop(self):
        if self.isEmpty():
            return None
        top_value = self.top.val
        self.top = self.top.next
        return top_value

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.val

    def display(self):
        curr = self.top
        while curr:
            print(curr.val, end = " -> ")
            curr = curr.next
        print("None")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()