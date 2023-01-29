"""
Write a function called longlengths that returns the lengths of those strings that have at least 4 characters. Try it with a 
list comprehension.
"""

#easy peasy
def longlengths(strings):
    return [len(i) for i in strings if len(i) > 4]

# esecuzione senza map e filter
def longlengths2(strings):
    new_lst = []
    for i in strings:
        if len(i)>=4:
            new_lst.append(len(i))
    return new_lst

#alternativa con map e filter
def longlengths3(strings):
    filtering = filter(lambda s: len(s) >= 4, strings)
    return map(lambda s: len(s),filtering)
            

lst =["a","bb","ccc", "dddd", "eeeee"]

print(longlengths(lst))





