"""
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which 
represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, 
positive_words to determine what words will count as positive. The function should return a positive integer - how many 
occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, 
so you’ll need to convert all the words in the input string to lower case as well.
"""




punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

            
def strip_punctuation(word):
    for i in word:
        if i in punctuation_chars:
            word=word.replace(i,"")
    return word

def get_pos(string):
    new_string = strip_punctuation(string)
    cont_occ = 0
    lower_string = new_string.lower()
    split_string = lower_string.split()
    for i in split_string:
        if i in positive_words:
            cont_occ+=1
    return cont_occ



            
    



