"""
Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent 
letter based on the dictionary. Assign this letter to the variable best_char.
"""


sally = "sally sells sea shells by the sea shore"
characters = {}
best_char = ""
for i in sally:
    if i not in characters:
        characters[i]=0
    characters[i]+=1


max = 0
for i in characters.values():
    if i > max:
        max=i
for key, value in characters.items():
    if max == value:
        best_char = key
print(best_char)