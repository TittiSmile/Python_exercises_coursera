"""
Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value. 
(Note: there is a builtin function named max but pretend you cannot use it.)
"""




import random as r
lst = []

for i in range(100):
    num = r.randint(1, 1000)
    lst.append(num)

def largest(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max

