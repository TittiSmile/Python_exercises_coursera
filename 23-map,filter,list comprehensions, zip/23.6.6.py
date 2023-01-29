# define lengths using map instead




def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
     of strings in the input list. Use map!"""
     # fill in this function's definition to make the test pass.
    return list(map(lambda i: len(i) , strings))
     
     
lst_strings=["ciao", "come", "stai", "bene", "grazie"]
print(lengths(lst_strings))