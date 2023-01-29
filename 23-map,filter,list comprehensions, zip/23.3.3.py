"""
Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
"""



lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
def filtering (lst):
    for i in lst:
        if "w" in i:
            return True
    return False
    


filter_testing = list(filter(lambda word: "w" in word,lst_check))
filter_testing2=list(filter(filtering,lst_check))

print(filter_testing)
print(filter_testing2)

#filter_testing2 è lo svolgimento senza appoggiarsi all'espressione lambda