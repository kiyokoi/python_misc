# -*- coding: utf-8 -*-
"""
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an 
ancestor of both nodes. For example, the root is a common ancestor of all 
nodes on the tree, but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. You can assume that 
both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), where T is 
the tree represented as a matrix, where the index of the list is equal to the 
integer stored in that node and a 1 represents a child node, r is a non-
negative integer representing the root, and n1 and n2 are non-negative 
integers representing the two nodes in no particular order. For example, one 
test case might be
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""

### Question4 main code
# Function to fine parents upto the root
def find_parent(T, node, ancestors):
    for i in range(len(T)):
        if T[i][node] == 1:
            parent = i
            ancestors.append(parent)
            find_parent(T, parent, ancestors)
    return ancestors

def question4(T, r, n1, n2):
    # Check for edge cases
    if not T or not r or not n1 or not n2:
        print "Invalid inputs!"
    else:        
        # Initialize the list of parents    
        ancestors1 = []
        ancestors2 = []
        ancestors1 = find_parent(T, n1, ancestors1)
        ancestors2 = find_parent(T, n2, ancestors2)
        
        if len(ancestors1) > len(ancestors2):
            longer_history = ancestors1
            shorter_history = ancestors2
        else:
            longer_history = ancestors2
            shorter_history = ancestors1
        
        # Compare the history line and output the lowest common ancestor    
        for i in range(len(longer_history)):
            for j in range(len(shorter_history)):
                if shorter_history[j] == longer_history[i]:
                    break
                return shorter_history[j]

### Question4 test cases
# Case 1: good example
T = [[0, 1, 0, 0, 0],\
     [0, 0, 0, 0, 0],\
     [0, 0, 0, 0, 0],\
     [1, 0, 0, 0, 1],\
     [0, 0, 0, 0, 0]]
r = 3
n1 = 1
n2 = 4
print question4(T, r, n1, n2)
# Expected output is 3

# Case 2: empty tree matrix
T = []
r = 3
n1 = 1
n2 = 4
print question4(T, r, n1, n2)
# Expected output is an error message: "Invalid inputs!"

# Case 3: any of r, n1 or n2 missing
T = [[0, 1, 1, 0, 0],\
     [0, 0, 0, 0, 0],\
     [0, 0, 0, 0, 0],\
     [1, 0, 0, 0, 1],\
     [0, 0, 0, 0, 0]]
r = 3
n1 = ''
n2 = 4
print question4(T, r, n1, n2)
# Expected output is an error message: "Invalid inputs!"