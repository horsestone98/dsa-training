# Creating a queue

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, val):
        new_node = Node(val)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        
        dequeued_val = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_val
    
    def peek(self):
        return None if self.isEmpty() else self.front.val
    
    def display(self):
        curr = self.front
        while curr:
            print(curr.val, end = " <- ")
            curr = curr.next
        print("None")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.display()