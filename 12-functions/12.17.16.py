#Sum up all the even numbers in a list.

def sumEven(lst):
    # your code here
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum+=i
    return sum
