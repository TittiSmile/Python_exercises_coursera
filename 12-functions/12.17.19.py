"""
Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it should 
return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)
"""


import math 

def findHypot(a,b):
    # your code here
    hypotenuse = math.sqrt((a**2)+(b**2))
    return hypotenuse

