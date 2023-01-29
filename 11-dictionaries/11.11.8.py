#Write a program that finds the most used 7 letter word in scarlet3.txt.


f = open('scarlet3.txt', 'r')
dic = {}  #dizionario che contienere quante volte le parole sono presenti nel file
reading = f.read()
splitted_words = reading.split()
for i in splitted_words: 
    if len(i) == 7: #con questa condizione garantisco solo le parole di 7 lettere
        if i not in dic:
            dic[i]=0
        dic[i]+=1
lst_key = list(dic.keys()) #creo una lista con tutte le chiavi
most_used = lst_key[0] #imposto come massimo il 1 valore della lista
for i in lst_key:
    if dic[i] > dic[most_used]:
        most_used = i
print(most_used)




