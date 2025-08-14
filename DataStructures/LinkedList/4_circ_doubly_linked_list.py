class CircDoublyNode():
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = CircDoublyNode(1)
A = CircDoublyNode(2, Head)
B = CircDoublyNode(3, A)
C = CircDoublyNode(4, B)
D = CircDoublyNode(5, C)

Head.prev = D
Head.next = A
A.next = B
B.next = C
C.next = D
D.next = Head

# 1. Displaying all the elements in the circular doubly linked list

def display_circdoublyll(first_value):
    curr = first_value
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next
        if curr == first_value:
            break

    print(" <-> ".join(elements))

# display_circdoublyll(Head)

# 2. Counting the elements in the circular doubly linked list

def count_circdoublyll(first_val):
    curr = first_val
    count = 0

    while curr:
        count += 1
        curr = curr.next
        if curr == first_val:
            break
    return count

# print(count_circdoublyll(Head))

# 3. Deleting an element in the circular doubly linked list in a specific position

def delete_circdoublyll(first_val, pos):
    if not first_val:
        return None

    cnt_value = count_circdoublyll(first_val)

    if pos < 0 or pos >= cnt_value:
        return first_val 

    if cnt_value == 1:
        return None

    if pos == 0:
        last = first_val
        while last.next != first_val:
            last = last.next
        first_val = first_val.next
        last.next = first_val
        first_val.prev = last

        return first_val

    curr = first_val
    for _ in range(pos):
        curr = curr.next
    curr.prev.next = curr.next
    curr.next.prev = curr.prev

    return first_val

# out1 = delete_circdoublyll(Head, 1)
# display_circdoublyll(out1)

# 4. Locating an element in a circular doubly linked list

def locate_circdoublyll(first_val, val):
    curr = first_val
    cnt_nodes = count_circdoublyll(first_val)
    pos = 0
    while curr and pos < cnt_nodes:
        if curr.val == val:
            return True
        curr = curr.next
        pos += 1
    return False

# out2 = locate_circdoublyll(Head, 21)
# print(out2)