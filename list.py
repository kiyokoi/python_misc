# -*- coding: utf-8 -*-
"""
Element generates single unit in a linked list.
"""


class Element(object):

    def __init__(self, value):
        self.value = value
        self.next = None

"""
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
"""


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        i = 1
        if position < 1:
            return None
        while i <= position:
            if i == position:
                return current
            else:
                current = current.next
                i += 1

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def delete_first(self):  # for Stack
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

    def insert(self, new_element, position):
        current = self.head
        i = 1
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        elif position > 1:
            while i < position:
                if i == (position - 1):
                    new_element.next = current.next
                    current.next = new_element
                    current = current.next
                    i += 1
                current = current.next
                i += 1

    def insert_first(self, new_element):  # for Stack
        new_element.next = self.head
        self.head = new_element


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

'''
Stack: built-in functions in python are pop() & append().
Add methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Why is it easier to add an "insert_first"
function than just use "append"?
'''


class Stack(object):

    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        self.ll.delete_first()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()
stack.push(e4)
print stack.pop()


"""Make a Queue class using a list.
Hint: You can use any Python list method
you'd like!"""


class Queue(object):

    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
print q.peek()  # 1

# Test dequeue
print q.dequeue()  # 1

# Test enqueue
q.enqueue(4)
print q.dequeue()  # 2
print q.dequeue()  # 3
print q.dequeue()  # 4
q.enqueue(5)
print q.peek()  # 5
