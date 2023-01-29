"""
Use manual accumulation to define the lengths function below.
"""

def lengths(lst_strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.
    return [len(i) for i in lst_strings]

lst_strings=["ciao", "come", "stai", "bene", "grazie"]
print(lengths(lst_strings))