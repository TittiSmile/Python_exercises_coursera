"""
Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. 
mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
"""

def addit(my_num):
    return my_num+5
    
def mult(my_num2):
    return my_num2*addit(my_num2)

#fai ATTENZIONE. è buona norma chiamare le variabili dei parametri con nomi diversi per evitare fraintendimenti
#le variabili my_num e my_num2 sono visibili SOLO nelle funzioni. va da sé che non posso richiamare addit con parametro my_num
#se avessi chiamato la variabile OVUNQUE my_num, python non avrebbe dato problemi. però non si capiva una ceppa. meglio EVITARE
#il parametro da passare ad addit, nella funzione mult, dovrà essere un numero o, al più, la variabile my_num2




