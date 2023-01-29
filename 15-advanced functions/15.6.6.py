"""
Write a function called together that takes three parameters, the first is a required parameter that is a number 
(integer or float), the second is a required parameter that is a string, and the third is an optional parameter 
whose default is ” “. What is returned is the first parameter, concatenated with the second, using the third.
"""


def nums(i, mult_int = 5, switch = False):
    if switch == True:
        return i*(-mult_int)
    else:
        return i*mult_int

