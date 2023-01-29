"""
Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
"""



nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 
          'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
for key, value in nested.items():
    if key=="data":
        data=True
        break
    else:
        data=False
        break
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
for key, value in nested.items():
    if key=="data":
        if 24 in value:
            twentyfour = True
            break
        else:
            twentyfour=False
            break
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
for key, value in nested.items():
    if key=="window":
        if "whole" in value:
            whole = False
            break
        else:
            whole=True
            break
    
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
for key, value in nested.items():
    if key=="physics":
        physics = True
        break
    else:
        physics=False
        break
