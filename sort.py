# -*- coding: utf-8 -*-

"""Write a binary search function.
You should use an iterative approach - meaning using loops.
Your function should take two inputs:
a Python list to search through, and the value you're searching for.
Assume the list only has distinct elements, meaning there are no repeated 
values, and elements are in a strictly increasing order.
Return the index of value, or -1 if the value doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high) / 2
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)


"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib_iter(position):
    if position == 0 or position == 1:
        return position
    first = 0
    second = 1
    next = first + second
    i = 2
    while i < position:
        first = second
        second = next
        next = first + second
        i += 1
    return next


def get_fib_recur(position):
    if position == 0 or position == 1:
        return position
    return get_fib_recur(position - 1) + get_fib_recur(position - 2)

# Test cases
print get_fib_iter(9)
print get_fib_iter(11)
print get_fib_iter(0)
print get_fib_recur(9)
print get_fib_recur(11)
print get_fib_recur(0)


"""Implement bubble sort in Python.
Input a list.
Output a sorted list."""


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print bubble_sort(test)
