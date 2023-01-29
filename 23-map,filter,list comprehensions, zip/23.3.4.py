"""
Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this.
"""


lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
def filtering (lst):
    for i in lst:
        if "o" in i:
            return True
    return False
lst2 = list(filter(lambda word: "o" in word,lst))
lst22 = list(filter(filtering,lst))
print(lst2)
print(lst22)