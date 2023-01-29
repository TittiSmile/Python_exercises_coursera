"""
Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown. 
The function should return a tuple that contains all the inputted information.
"""


def info(name, age, birth_year, year_in_college, hometown):
    return name, age, birth_year, year_in_college, hometown




"""
un po' di teoria:
in python è possibile far ritornare ad una funzione 2 valori. in realtà la funzione stessa ritornerà SEMPRE 1 solo valore (non è
possibile far tornare 2 cose da una funzione) però raggruppato in una tupla.
quindi tutto quel big return, non è che ritorna un nome, l'età, la data di nascita etc. NO. ritornerà solo una tupla con tutte
queste informazioni

"""