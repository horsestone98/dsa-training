class DoublyNode():
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = DoublyNode(1, None)
A = DoublyNode(2, Head)
B = DoublyNode(3, A)
C = DoublyNode(4, B, None)
B.next = C
Head.next = A
A.next = B
Tail = C

# 1. Displaying the elements in the doubly linked list using '<->'

def display_doublyll(first_val):
    elements = []
    while first_val:
        elements.append(str(first_val.val))
        first_val = first_val.next
    print(' <-> '.join(elements))

# display_doublyll(Head)

# 2. Search for a value in a doubly linked list and its position
# ----- Approach 1: Search the values from the first node -----

def searchval_first_doublyll(first_val, search_val):
    curr = first_val
    value = 0
    while curr:
        value += 1
        if curr.val == search_val:
            return True, value
        curr = curr.next
    return False

# print(searchval_first_doublyll(Head, 10))

# ----- Approach 2: Search the values from the last node -----

def searchval_last_doublyll(last_val, search_val):
    curr = last_val
    value = 0
    while curr:
        value += 1
        if curr.val == search_val:
            return True, value
        curr = curr.prev
    return False

# print(searchval_last_doublyll(Tail, 1))

# 3. Add an element to a specific position

def insert_val_dl(first_val, insert_val, pos):
    new_node = DoublyNode(insert_val)

    if pos <= 0:
        new_node.next = first_val
        first_val.prev = new_node

        return new_node
    
    curr = first_val
    index = 0

    while curr and index < pos - 1:
        curr = curr.next
        index += 1
    
    if not curr:
        return first_val
    
    new_node.next = curr.next
    new_node.prev = curr
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node

    return first_val

# out1 = insert_val_dl(Head, 7, 1)
# display_doublyll(out1)

# 4. Reverse the doubly linked list

def reverse_dl(first_val):
    curr = first_val
    prev = None

    while curr:
        # Swap next and prev for the current node
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        
        # Move prev to current, and current to its new prev (old next)
        prev = curr
        curr = curr.prev
    
    # After the loop, prev will be at the new head
    return prev


# out5 = reverse_dl(Head)
# display_doublyll(out5)