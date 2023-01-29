#Define longwords using filter.



def longwords_Fil(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use the filter function."""
    # write your code here
    return list(filter(lambda i: len(i)>4, strings ))

