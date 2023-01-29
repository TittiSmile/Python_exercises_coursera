initial = 7
def f(x, y = 3, z = initial):
    print ("x, y, z are:", x, y, z)
initial = 0
f(2)



"""
allora, questa funzione prende 3 parametri. due dei quali (y z) hanno dei valori di default quindi, quando vai ad invocarla, puoi
anche non specificare i loro valori. saranno presi, di default, quelli specificati nella firma del metodo.
di seguito, invocazioni LEGIT:

f(10,4,6) 
f(2, 5)         #x assume il valore di 2 e y quello di 5. il valore di z sarà quello dato di default
f("ciao", "come", "va")
f(1,2)
f(1,z=4)    #in questo caso, y avrà il suo valore di default e z prenderà 4
f(1,y=5)    #come sopra, solo che c'è y
f(x=10,y=4,z=6)  # un po' superfluo mettere x=, y=... però ha senso
f(z=4,x=7,y=3) #anche se l'ordine è sballato, va bene uguale.



di seguito, invocazioni SBAGLIATE:

f(z=8)      #errore perchè x è il parametro che va messo per forza (non ha valore di default)
f(y=9,y=6)  #errore. hai messo due volte y
f(x=10,2)   #come sotto
f(10,x=3)   #errore perchè si dà per scontato che 10 è assegnato per x ma subito dopo il suo valore viene impostato a 3. quindi 
            i parametri opzionali (quelli con = nella dichiarazione) vanno messi DOPO quello obbligatorio (cioè x)
f(z=1,10)   #qui si va ad intendere che x ha il valore di 10 e z di 1. ERRORE perchè, come detto sopra, i parametri opzionali
            vanno dopo quelli obbligatori. nella dichiarazione di f() x viene prima di z
"""