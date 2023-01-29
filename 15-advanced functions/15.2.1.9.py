
def waste(mar, var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string


"""
questo esercizio aveva un errore. il metodo era il seguente:

def waste(var = "Water", mar, marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string


il problema era che mar, variabile RICHIESTA, era messa dopo una variabile con 
valore di default. questa cosa non è possibile!!!
i parametri richiesti (quelli senza valore di default) vanno messi per primi!!!
"""