"""
Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. 
The second is an optional parameter called direction with a default value of True. The third is an optional parameter 
called d that has a default value of 
{'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. 
Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is 
a key in the third parameter; if it is, return True, otherwise return False.

But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. 
If it’s not, the function should return True in this case, and if it is, it should return False.
"""




def checkingIfIn(s, direction=True, d={'apple': 2, 'pear': 1, 
                                       'fruit': 19, 'orange': 5, 
                                       'banana': 3, 'grapes': 2, 
                                       'watermelon': 7}):
    flag = False
    if direction == True:
        for key, value in d.items():
            print(key, "    ", value)
            if s == key:
                flag = True
                break
            else:
                flag = False
    else:
        for key, value in d.items():
            print(key, "    ", value)
            if s != key:
                flag =  True
            else:
                flag = False
                break
    return flag
    