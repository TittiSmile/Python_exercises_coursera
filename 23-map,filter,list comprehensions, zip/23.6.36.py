"""
Challenge The nested for loop given takes in a list of lists and combines the elements into a single list. 
Do the same thing using a list comprehension for the list L. Assign it to the variable result2.


"""




def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]

#print(onelist(L))

def onelist_comp(lst):
    #return [[number for number in group] for group in lst] #questo serve se hai una lista e VUOI una lista di liste
    return[item for sublist in lst for item in sublist]     #questo serve se hai una lista di liste e VUOI una lista
print(onelist_comp(L))
