"""
Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.
"""




string = str(input("write a sentence"))
lst_key = []
dictionary = {"is":"be", "man":"matey", "hello":"avast", "my":"me", 
              "restoom":"head", "the":"th", "lawyer":"foul blaggart",
              "are":"be", "students":"swabbies", "excuse":"arr", 
              "your":"yer","restaurant":"gallery","professor":"foul blaggart",
              "madam":"proud beauty", "boy":"matey", "student":"swabbie",
              "hotel":"fleabag inn","sir":"matey"}
dict_keys = list(dictionary.keys())
splitted_string = string.split()
for i in splitted_string: 
    if i in dict_keys: 
        lst_key.append(i)
str_translate = ""
for i in lst_key:
    if i in dict_keys:
        str_translate += dictionary[i]+" "
print(str_translate)


