"""
Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains 
all the same strings in upper case.
"""



abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def upper(string):
    return string.upper()

abbrevs_upper = list(map(upper,abbrevs)) #è importante il casting sennò non esce il risultato giusto :D

abbrevs_upper2 = list(map(lambda val: val.upper(), abbrevs))

print(abbrevs_upper)
print(abbrevs_upper2)