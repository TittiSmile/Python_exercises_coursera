"""
Create a dictionary called d that keeps track of all the characters in the string placement and notes how 
many times each character was seen. Then, find the key with the lowest value in this dictionary and assign 
that key to min_value.
"""

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
min = 1000
d = {}

#popolo il dizionario. ogni lettera ha il suo numero di occorrenze
for i in placement:
    if i not in d:
        d[i]=0
    d[i]+=1

#cerco il minimo nel dizionario
for i in d:
    if d.get(i) < min:
        min = d.get(i)

#vado a cercare la chiave associata a quel minimo. uso la funzione items.
#funziona come il ciclo for in java con le mappe
min_value=""       
for key, value in d.items():
    if min == value:
        min_value=key





###versione alternativa###
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
min = 1000
d = {}

#popolo il dizionario. ogni lettera ha il suo numero di occorrenze
for c in placement:
    if c not in d:
        d[c]=0
    d[c]+=1

keys = list(d.keys()) #creo una lista con dentro tutte le chiavi.
min_value = keys[0] # impongo che il minimo sia il primo valore della lista

for key in keys:
    if d[key] < d[min_value]:
        min_value=ke