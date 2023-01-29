"""
Write a function called positives_Acc that receives list of numbers as the input (like [3, -1, 5, 7]) and returns a list of 
only the positive numbers, [3, 5, 7], via manual accumulation.


"""


things = [3, 5, -4, 7]

def positives_Acc(lst):
    return [i for i in lst if i>0]
    
print(positives_Acc(things))