# -*- coding: utf-8 -*-
"""
Given two strings s and t, determine whether some anagram of t 
is a substring of s. For example: if s = "dogncat" and t = "act", 
then the function returns True. Your function definition should 
look like: question1(s, t) and return a boolean True or False.
"""
from collections import Counter

### Question1 main code
def question1(s, t):
    if len(t) > len(s) or len(t) == 0 or len(s) == 0:
        print "Invalid inputs!"
    else:
        count = 0
        s = s.lower()
        t = t.lower()
        for i, c in enumerate(s):
            window = s[i:i+len(t)]
            if Counter(t) == Counter(window):
                count += 1
        if count > 0:
            return True
        return False

### Question1 test cases
# Case 1: good example
s = 'RabbitHole'
t = 'hit'
print question1(s, t)
# Expected output is True
    
# Case 2: t is longer than s
s = 'rabbit'
t = 'rabbithole'
print question1(s, t)
# Expected output is an error message: "Invalid inputs!"

# Case 3: t is empty
s = 'rabbithole'
t = ''
print question1(s, t)
# Expected output is an error message: "Invalid inputs!"
