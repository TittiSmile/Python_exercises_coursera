"""
Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using an accumulator 
pattern.


"""




def sumSquares(L):
    num = 0
    for i in L:
        num+=i**2
    return num

nums = [3, 2, 2, -1, 1]

