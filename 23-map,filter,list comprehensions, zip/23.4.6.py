"""
Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary 
tester. Do this using a list comprehension.
"""	




tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, 
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, 
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, 
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, 
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri = []

for key, value in tester.items():
    for lst in value:
        for elem in lst:
            compri.append(lst["name"])
            break		#lo metto perchè sennò mi inseriva tante volte quante entità nel dizionario corrente
print(compri)

#se vuoi usare le nozioni appena imparate (filtri e list comprehension)


import json
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, 
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, 
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, 
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, 
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

print(json.dumps(tester["info"], indent=2)) # serve a dare un segno di lettura migliore. inoltre stampa solo i valori della chiave info
compri = [d["name"] for d in tester["info"]]
print(compri)


