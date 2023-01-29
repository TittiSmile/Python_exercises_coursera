"""
Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how 
many times each character was seen. Then, find the key with the highest value in this dictionary and assign that 
key to max_value.
"""

#funziona come quello del minimo. solo che c'è il massimo impostato a 0 e > invece di <
product = "iphone and android phones"
lett_d = {}
max = 0


for i in product:
    if i not in lett_d:
        lett_d[i]=0
    lett_d[i]+=1

for i in lett_d:
    if lett_d.get(i) > max:
        max = lett_d.get(i)

max_value=""       
for key, value in lett_d.items():
    if max == value:
        max_value=key






#####versione alternativa
product = "iphone and android phones"
lett_d = {}

for c in product:
    if c not in lett_d:
        lett_d[c]=0
    lett_d[c]+=1

keys = list(lett_d.keys())
max_value = keys[0]

for k in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key




