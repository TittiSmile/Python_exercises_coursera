"""
Now sort the keys (numbers) based on their frequencies. Review Sorting a Dictionary if you’re not sure how to do this. 
Keep just the top five keys.
"""



L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]
d={}

def return_values(k):
    return d[k]

def dictionary_counts(s):
    for i in L:
        if i not in d:
            d[i] = 0
        d[i]+=1
    sv = (sorted(d.keys(), key=return_values, reverse=True))
        
    return sv

new_dic = dictionary_counts(L)
print(new_dic)