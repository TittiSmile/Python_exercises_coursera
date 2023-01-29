"""
Write code to assign to the variable compri_sample all the values of the key name in the dictionary tester if they are Juniors. 
Do this using list comprehension.


"""
import json
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, 
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, 
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, 
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, 
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
                   
info = tester["info"]
info_indent =  json.dumps(tester["info"], indent=2)
compri_sample=[dic["name"] for dic in info if dic["class standing"] == "Junior"]
print(compri_sample)
                   