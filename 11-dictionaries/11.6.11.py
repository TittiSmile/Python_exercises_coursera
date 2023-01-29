"""
Create a dictionary called char_d. The keys of the dictionary should be each character in stri, and the value for 
each key should be how many times the character occurs in the string.
"""


stri = "what can I do"
char_d={}

for i in stri:
    char_d[i] = char_d.get(i,0)+1


###################################
#è un modo equivalente di fare l'esercizio

stri = "what can I do"
char_d={}

for i in stri:
    if i not in char_d:
        char_d[i]=0
    char_d[i]+=1
print(char_d)

#questa roba qua si chiama "accumulation pattern"
