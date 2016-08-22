# -*- coding: utf-8 -*-
"""
Find the element in a singly linked list that's m elements from the end. For 
example, if a linked list has 5 elements, the 3rd element from the end is the 
3rd element. The function definition should look like question5(ll, m), where 
ll is the first node of a linked list and m is the "mth number from the end". 
Return the value of the node at that position."""

# Question5 main code
# Define Node class


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

# Define LinkedList class for the operations on the linked list


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        new_node = Node(new_element)
        new_node.next = self.head
        self.head = new_node

    def question5(self, ll, m):
        if not ll or not m:
            return "Invalid inputs!"
        else:
            val = ll
            for i in range(m):
                val = val.next
            if val is None:
                return ll.data
            else:
                return self.question5(ll.next, m)

# Question5 test cases
# Case 1: good example
l = LinkedList()
l.append(12)
l.append(1)
l.append(2)
l.append(25)
l.append(16)

m = 3
ll = l.head
print l.question5(ll, m)
# Expected output is 2

# Case 2: missing ll
l = LinkedList()
l.append(20)
l.append(4)
l.append(15)
l.append(27)
l.append(16)

m = 3
ll = ''
print l.question5(ll, m)
# Expected output is an error message: "Invalid inputs!"

# Case 3: missing m
l = LinkedList()
l.append(20)
l.append(4)
l.append(15)
l.append(27)
l.append(16)

m = ''
ll = l.head
print l.question5(ll, m)
# Expected output is an error message: "Invalid inputs!"
