# Singly Linked List

class SinglyNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
D = SinglyNode(5)
E = SinglyNode(6)

Head.next = A
A.next = B
B.next = C
C.next = D
D.next = E

# 1. Creating a linked list in a set

def lst_vals(start_node):
    curr = start_node
    final_lst = []
    while curr:
        final_lst.append(curr.val)
        curr = curr.next
    return final_lst

# print(lst_vals(Head))

# 2. Printing a singly linked list using '->'

def display_singlyll(head_val):
    curr = head_val
    set_val = []
    while curr:
        set_val.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(set_val))

# display_singlyll(Head)

# 3. Search for a value and its position in a linked list

def searchval_singlyll(first_val, search_val):
    curr = first_val
    pos = 0
    while curr:
        pos += 1
        if search_val == curr.val:
            return True, pos
        curr = curr.next
    return False

# print(searchval_singlyll(Head, 1))

# 4. Remove an element in a specified position

def remove_val_sl(first_val, remove_pos):
    if remove_pos < 0:
        return first_val
    
    if remove_pos == 0:
        return first_val.next

    curr = first_val
    count = 0

    while curr and count < remove_pos - 1:
        curr = curr.next
        count += 1
    
    if not curr or not curr.next:
        return first_val
    
    curr.next = curr.next.next
    return first_val

# out1 = remove_val_sl(Head, 4)
# display_singlyll(out1)

# 5. Add a new element in a specified position

def insert_val_sl(first_val, insert_val, pos):
    new_node = SinglyNode(insert_val)

    if pos <= 0:
        return new_node
    
    curr = first_val
    count = 0

    while curr and count < pos - 1:
        curr = curr.next
        count += 1
    
    if not curr:
        return first_val
    

    new_node.next = curr.next
    curr.next = new_node
    
    return first_val

# out2 = insert_val_sl(Head, 9, 1)
# display_singlyll(out2)

# 6. Reverse a singly linked list.  

def singly_reverse(first_val):
    prev = None
    curr = first_val

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev

# out3 = singly_reverse(Head)
# display_singlyll(out3)

# 7. Sum of all node values of a singly linked list

def sum_singlyll(first_val):
    curr = first_val
    temp = 0
    while curr:
        temp += curr.val
        curr = curr.next
    return temp

# print(sum_singlyll(Head))

# 8. Product of all node values of a singly linked list

def product_singlyll(first_val):
    curr = first_val
    temp = 1
    while curr:
        temp *= curr.val
        curr = curr.next
    return temp

print(product_singlyll(Head))

# 9. Concatenate all the values of a singly linked list

def concat_singlyll(first_val):
    curr = first_val
    val = ''
    while curr:
        val = val + str(curr.val)
        curr = curr.next
    return val

# print(concat_singlyll(Head))