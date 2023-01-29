"""
Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a 
sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 
(it should not contain the number 5).

"""
def sublist(num_lst):
    new_lst = []
    i = 0
    while i < len(num_lst):
        if num_lst[i] == 5:
            break
        else:
            new_lst.append(num_lst[i])
        i+=1
    return new_lst
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(sublist(lst))