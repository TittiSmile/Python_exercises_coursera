"""
Define a function called nums that has three parameters. The first parameter, an integer, should be required. 
A second parameter named mult_int should be optional with a default value of 5. The final parameter, switch, 
should also be optional with a default value of False. The function should multiply the two integers together, 
and if switch is True, should change the sign of the product before returning it.
"""



def nums(i, mult_int = 5, switch = False):
    if switch == True:
        return i*(-mult_int)
    else:
        return i*mult_int

