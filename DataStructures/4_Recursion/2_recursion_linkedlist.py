class RecursionClass:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = RecursionClass(1)
A = RecursionClass(2)
B = RecursionClass(3)
C = RecursionClass(4)
D = RecursionClass(5)

Head.next = A
A.next = B
B.next = C
C.next = D

# 1. Printing the elements in the linked list

def printrecval(head):
    if head is None:
       return ""
    if head.next is None:
        return str(head.val)
    
    return str(head.val) + " -> " + printrecval(head.next)

# print(printrecval(Head))

# 2. Length of linked list

def length(head):
    if head is None:
        return 0
    return 1 + length(head.next)

# print(length(Head))

# 3. Search an element

def searchvalue(head, searchval):
    if head is None:
        return
    if head.val == searchval:
        return True
    return searchvalue(head.next, searchval)

# print(searchvalue(Head,6))

# 4. Sum of elements

def sumvals(head):
    if head is None:
        return 0
    return head.val + sumvals(head.next)

# print(sumvals(Head))

# 5. Reversing the singly linked list

def reverse(head):
    if head is None or head.next is None:  # Base: empty or last node
        return head
    new_head = reverse(head.next)   # Reverse rest
    head.next.next = head           # Put current at end
    head.next = None
    return new_head

# out1 = reverse(Head)
# print(printrecval(out1))