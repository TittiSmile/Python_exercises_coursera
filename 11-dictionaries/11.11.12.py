"""
Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet 
in alphabetical order which occur in the string together with the number of times each letter occurs. 
Case should be ignored. A sample run of the program might look this this:
"""

string = "ThiS is String with Upper and lower case Letters"
converted_string = string.lower()
dic = {}
for i in converted_string:
    if i not in dic:
        dic[i]=0
    dic[i]+=1

lst_key = list(dic.keys())
ordered_key = sorted(lst_key)
sorted_dic = {}
for i in ordered_key:
    sorted_dic[i] = dic[i]
print(sorted_dic)

#creare un nuovo dizionario uguale all'altro può essere dispensioso a livello di costi ma non avevo un'altra soluzione :D