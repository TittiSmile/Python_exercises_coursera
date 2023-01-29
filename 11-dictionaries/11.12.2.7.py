"""
Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. 
Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
"""

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
worst_char = ""
for i in sally:
    if i not in characters:
        characters[i]=0
    characters[i]+=1


min = 10000
for i in characters.values():
    if i < min:
        min=i
for key, value in characters.items():
    if min == value:
        worst_char = key
print(worst_char)
