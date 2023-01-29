"""
Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
"""

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
splitted_string = str1.split()
for i in splitted_string:
    if i not in freq_words:
        freq_words[i]=0
    freq_words[i]+=1
print(freq_words)
