# -*- coding: utf-8 -*-
"""
Given a string a, find the longest palindromic substring contained 
in a. Your function definition should look like question2(a), and 
return a string
"""
### Question2 main code
def question2(a):
    if len(a) == 0 or len(a) > 45:
        print "Invalid inputs!"
    else:
        a = a.lower()        
        solution_list = []
        for i in range(len(a)):
            j=0
            while j < i:
                letters = a[j:i]
                if letters == letters[::-1]:
                    solution_list.append(letters)
                j += 1
        return max(solution_list, key=len)

### Question2 test cases
# Case 1: good example
a = 'bananas'
print question2(a)
# Expected output is 'anana'

# Case 2: a is empty
a = ''
print question2(a)
# Expected output is an error message: "Invalid inputs!"

# Case 3: 
a = 'HippopotomonstrosesquipedaliophobiaFloccinaucinihilipilification'
print question2(a)
# Expected output is an error message: "Invalid inputs!"

