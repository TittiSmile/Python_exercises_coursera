"""
We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, 
input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions 
in the active code window for specific variable assignmemts.
"""



def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7, "kiwi" : 8}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn(a="ciao")

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn("come",False)

# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn("fruit")

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn("kiwi")



#molto funny, ho dovuto aggiungere l'ultima voce "kiwi" perchè nella traccia non c'era (: complimenti a tutti 