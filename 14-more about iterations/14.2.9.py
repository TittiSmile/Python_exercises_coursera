"""
Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a 
new list until the number 4 appears. The function should return the new list.
"""


def stop_at_four(lst):
    new_lst = []
    i = 0
    while i < len(lst):
        
        if(lst[i] == 4):
            break
        else:
            new_lst.append(lst[i])
        i += 1
    return new_lst


lst = [0, 9, 4.5, 1, 7, 4, 8, 9, 3]
print(stop_at_four(lst))

