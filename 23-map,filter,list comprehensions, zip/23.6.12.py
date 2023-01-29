"""
Write a function called positives_Fil that receives list of things as the input and returns a list of only the positive things, 
[3, 5, 7], using the filter function.


"""

things = [3, 5, -4, 7]


def positives_Fil(lst):
    return list(filter(lambda i: i  > 0, things ))
    
print(positives_Fil(things))