# -*- coding: utf-8 -*-
"""
Given a string a, find the longest palindromic substring contained 
in a. Your function definition should look like question2(a), and 
return a string
"""
# Question2 main code


def question2(a):
    if len(a) == 0:
        print "Invalid inputs!"
    else:
        a = a.lower()
        longest = a[0]
        palindrome = a[0]
        for i in range(len(a)):
            for j in range(i):
                letters = a[j:i + 1]
                if letters == letters[::-1]:
                    palindrome = letters
                    if len(palindrome) > len(longest):
                        longest = palindrome
        return longest

# Question2 test cases
# Case 1: good example
a = 'bananas'
print question2(a)
# Expected output is 'anana'

# Case 2: a is empty
a = ''
print question2(a)
# Expected output is an error message: "Invalid inputs!"

# Case 3: capital letters
a = 'RACECAR'
print question2(a)
# Expected output is an error message: "Invalid inputs!"
