#Define longwords using manual accumulation.

def longwords(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use manual accumulation."""
    # write your code here
    return [i for i in strings if len(i)>4]
