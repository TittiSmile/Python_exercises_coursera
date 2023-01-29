"""
Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
"""


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def double(my_list):
    new_list = []
    for i in my_list:
        #print(i)
        #print(type(i))
        new_list.append(i*2)
    return new_list

a=double(lst)
print(a)
greeting_doubled = map(double ,lst)

print(list(greeting_doubled)) #errore


# c'è un ERRORE!!!! per stampare greeting_doubled c'è bisogno di fare un cast altrimenti mi esce <map object at ...>
# peccato che la lista lst non è seplicemente una lista. al suo interno ci sono liste, stringhe e pure numeri
#castare semplicemente il tutto a list è riduttivo perchè andrà bene solo per i valori che sono effettivamente liste :D
#COME SI RISOLVE?



#POSSIBILE soluzione:


lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = list(map(lambda value:2*value ,lst))


