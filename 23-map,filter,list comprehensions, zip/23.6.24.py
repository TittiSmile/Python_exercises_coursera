"""
Write a function called longlengths that returns the lengths of those strings that have at least 4 characters. Try it using 
map and filter.


"""


lst =["a","bb","ccc", "dddd", "eeeee"]

def longlengths(strings):
    filtering = list(filter(lambda s: len(s) >= 4, strings))
    return list(map(lambda s: len(s),filtering))
    
            
            
print(longlengths(lst))