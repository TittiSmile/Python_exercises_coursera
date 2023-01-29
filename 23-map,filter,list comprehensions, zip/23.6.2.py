"""
Write equivalent code using map instead of the manual accumulation below and assign it to the variable test.
"""



things = [3, 5, -4, 7]

accum = []
for thing in things:
    accum.append(thing+1)
print(accum)

#parte fatta da me:

test = list(map(lambda x : x+1,things))
print(test)





########
#pensavo potesse andare bene anche così MA
my_list = []
a = foo(my_list)
#print(a)

b = list(map(foo, things))
#print(b)

#MA il 1 print va bene (ma non c'è map)
#il secondo print mi stampa le cose giuste ma tante volte quanti sono gli elementi nella lista things quindi no bueno


