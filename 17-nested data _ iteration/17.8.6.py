"""
Below, we have provided a nested list called big_list. Use nested iteration to create a dictionary, word_counts, 
that contains all the words in big_list as keys, and the number of times they occur as values
"""



big_list = [[['one', 'two'], ['seven', 'eight']],
            [['nine', 'four'], ['three', 'one']], 
            [['two', 'eight'], ['seven', 'four']], 
            [['five', 'one'], ['four', 'two']], 
            [['six', 'eight'], ['two', 'seven']], 
            [['three', 'five'], ['one', 'six']], 
            [['nine', 'eight'], ['five', 'four']], 
            [['six', 'three'], ['four', 'seven']]]
word_counts = {}
cont = 0
for lst in big_list:
    for elem in lst:
        for val in elem:
            #print(val)
            if val not in word_counts:
                word_counts[val]=0
            word_counts[val]+=1
print(word_counts)