"""
Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and
the number of times it occurs.
"""

s1 = "hello"
counts={}
for i in s1:
    if i not in counts:
        counts[i]=0
    counts[i]+=1
print(counts)
    
