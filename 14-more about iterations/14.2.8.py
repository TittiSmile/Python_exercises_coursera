"""
Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, 
but instead uses a while loop. Assign the accumulator variable to the name accum.
"""


list1 = [8, 3, 4, 5, 6, n7, 9]

tot = 0
for elem in list1:
    tot = tot + elem


accum = 0
i=0
while i < len(list1):
    accum += list1[i]
    i += 1



"""
ok in questo esercizio si vede facilmente come while e for funzionano diversamente.
nel FOR stiamo scorrendo la lista con elem (un intero). il valore di elem, ad ogni iterazione, sarà uguale all'elemento i-esimo
della lista (quindi 8, 3, 4...)
nel WHILE il valore di i sarà un valore da 0 - lunghezza lista. il valore corrente di i NON sarà il valore presente nella lista.
infatti il valore corrente lo si ottiene facendo list1[i]

"""