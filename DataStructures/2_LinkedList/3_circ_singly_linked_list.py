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

Head.next = A
A.next = B
B.next = C
C.next = D
D.next = Head

# 1. Printing the circular singly linked list 

def display_circsinglyll(first_val):
    curr = first_val
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next
        if curr == first_val:
            break

    print(' -> '.join(elements))

# display_circsinglyll(Head)

# 2. Counting the elements in a circular singly linked list

def count_circsinglyll(first_val):
    curr = first_val
    count = 0
    while curr:
        count += 1
        curr = curr.next
        if curr == first_val:
            break
    return count

# print(count_circsinglyll(Head))


# 2. Deleting an element from a specified position in the circular singly linked list

def deleteval_circsinglyll(first_val, pos):
    if not first_val:
        return None  # Empty list

    cnt_val = count_circsinglyll(first_val)

    # If invalid position
    if pos < 0 or pos >= cnt_val:
        return first_val

    # Single node case
    if cnt_val == 1:
        return None

    curr = first_val

    # Deleting head
    if pos == 0:
        # Find last node
        last = first_val
        while last.next != first_val:
            last = last.next
        # Move head to next node
        first_val = first_val.next
        last.next = first_val
        return first_val
    # Deleting a non-head node
    count = 0
    while count < pos - 1:
        curr = curr.next
        count += 1

    curr.next = curr.next.next
    return first_val

# out3 = deleteval_circsinglyll(Head, 1)
# display_circsinglyll(out3)

# 3. Inserting a node in a circular singly linked list at a particular position

def insertval_circsinglyll(first_val, insert_val, pos):
    new_node = CircSinglyNode(insert_val)
    cnt_value = count_circsinglyll(first_val)

    if pos < 0:
        return first_val
    
    if pos == 0:
        last = first_val
        while last.next != first_val:
            last = last.next
        last.next = new_node
        new_node.next = first_val

        return new_node

    
    if pos > 0:
        curr = first_val
        value = 0

        if pos < cnt_value:
            while curr and value < pos - 1:
                curr = curr.next
                value += 1
            
            new_node.next = curr.next
            curr.next = new_node

        else:
            while curr.next != first_val:
                curr = curr.next
            curr.next = new_node
            new_node.next = first_val

        return first_val

# out6 = insertval_circsinglyll(Head, 9, 5)
# display_circsinglyll(out6)

# 4. Locating an element in the circular singly linked list

def locate_circsinglyll(first_value, val):
    cnt_val = count_circsinglyll(first_value)

    curr = first_value
    pos = 0
    while curr and pos < cnt_val:
        if curr.val == val:
            return True, pos
        curr = curr.next
        pos += 1
    return False


# print(locate_circsinglyll(Head, 3))