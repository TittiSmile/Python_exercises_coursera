"""
You’re going to write a function that takes a string as a parameter and returns a list of the five most frequent characters in 
the string. Eventually, you will be able to do this sort of problem without a lot of coaching. But we’re going to step you 
through it as a series of exercises.

First, the function will count the frequencies of all the characters, as we’ve done before, using a dictionary and the 
accumulator pattern. Then, it will sort the (key, value) pairs. Finally, it will take a slice of the sorted list to get 
just the top five. That slice will be returned.

Step 1. Suppose you had this list, [8, 7, 6, 6, 4, 4, 3, 1, 0], already sorted, how would you make a list of just the best 5? 
(Hint: take a slice).
"""

d = {}
L = [8, 7, 6, 6, 4, 4, 3, 1, 0]

def return_values(k):
    return d[k]

def function(s):

    for i in L:
        if i not in d:
            d[i] = 0
        d[i]+=1
    sv = (sorted(d.keys(), key=return_values, reverse=True))
    return sv
    
print(function(L))









