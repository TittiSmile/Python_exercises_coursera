"""
Split the string sentence into a list of words, then create a dictionary named word_counts that contains each word and the 
number of times it occurs.
"""



sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
splitted = sentence.split()
word_counts = {}

for i in splitted:
    word_counts[i] = word_counts.get(i,0)+1


    

