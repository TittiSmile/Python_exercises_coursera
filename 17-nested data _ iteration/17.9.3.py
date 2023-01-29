"""
Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode 
window for further directions.
"""



L = [[5, 8, 7], 
     ['hello', 'hi', 'hola'], 
     [6.6, 1.54, 3.99], 
     ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for i in L:
    if "hola" in L:
        test1= True
    else:
        test1= False
# Test if [5, 8, 7] is in the list L. Save to variable name test2
for i in L:
    if [5,8,7] in L:
        test2= True
    else:
        test2= False
# Test if 6.6 is in the third element of list L. Save to variable name test3

if 6.6 in L[2]:
    test3= True
else:
    test3= False
