#Write a function to count how many odd numbers are in a list.




def countOdd(lst):
    # your code here
    sum = 0
    for i in lst:
        if i % 2 == 1:
            sum+=1
    return sum

