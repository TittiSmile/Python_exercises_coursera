"""
Write a function called str_mult that takes in a required string parameter and an optional integer parameter. 
The default value for the integer parameter should be 3. The function should return the string multiplied by the 
integer parameter.
"""


def str_mult(string, integer = 3):
    return string * integer


#il secondo parametro è quello facoltativo (ha un valore di default impostato) che ha un valore di default. ovviamente puoi 
#anche cambiarglielo quando invochi la funzione. 

#ecco alcune invocazioni totalmente LEGIT.

str_mult("ciao",5)
str_mult("hello") #valore di default 3