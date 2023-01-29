"""
The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more 
errors in it. Use this space to write test cases to determine what errors there are. You will be using this information to 
answer the next set of multiple choice questions.

"""


import test

def mySum (lst_num):
    sum = 0
    for i in lst_num:
        sum+=i
    return sum

#per controllare che sia una lista di interi
lst = [1,2,3]
first_type = type(lst[0])
for item in lst:
    assert type(item) == first_type