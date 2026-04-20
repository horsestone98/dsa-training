# This notebook is created to understand the basic of binary tree and its traversal

# Binary Tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. 
# It is a hierarchical data structure that is used to represent relationships between data elements.
# The basic properties of a binary tree are as follows:
# 1. Each node in a binary tree has at most two children.
# 2. The topmost node of the tree is called the root node.
# 3. Each child node can have at most two children of its own, and so on, creating a hierarchical structure.
# 4. The depth of a node is the number of edges from the root to the node.
# 5. The height of a node is the number of edges on the longest path from the node to a leaf.
# 6. A binary tree can be classified as a full binary tree, a complete binary tree, or a perfect binary tree based on its structure.
# 7. Binary trees are commonly used in various applications such as expression parsing, binary search trees, heaps, and more.

# Let's implement a basic binary tree in Python and perform some traversals on it.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


#        1
#     2    3
#   4  5  10


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# Recursive Pre Order Traversal (DFS)
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)