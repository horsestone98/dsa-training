class CircSinglyNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

Head = CircSinglyNode(1)
A = CircSinglyNode(2)
B = CircSinglyNode(3)
C = CircSinglyNode(4)
D = CircSinglyNode(5)
E = CircSinglyNode(6)
F = CircSinglyNode(7)
G = CircSinglyNode(8)
H = CircSinglyNode(9)

Head.next = A
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H
H.next = B

# printing the values of circular singly linked list

def countlength_loop(first_val):
    slow = first_val
    fast = first_val

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    count = 0
    while fast:
        count += 1
        fast = fast.next
        if fast == slow:
            break
    return count

print(countlength_loop(Head))