def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked
#print(add(z,8))    #questo andrebbe bene!!!!



"""
se non avessi messo * vicino a z mi avrebbe dato errore.
questo perchè il metodo add prende 2 parametri in ingresso. z è una singola tupla con due parametri. 
erroneamente si potrebbe pensare che potrebbero fungere da variabili di passaggio (x=5 y=4). ovviamente è SBAGLIATO.
se metto * sto dicendo di impacchettare i valori 5 e 4 come se fossero effettivamente x e y del metodo add.
senza, sarebbe errore perchè è come se add prendesse come parametro solo z 
"""