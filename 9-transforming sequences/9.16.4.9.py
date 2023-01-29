"""
Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign 
the answer to a variable num_words_list. (You should use the len function).
"""



original_str = "The quick brown rhino jumped over the extremely lazy fox"
cont=0
num_words_list=[]
for i in original_str:
    s = original_str.split(" ")
for j in range(len(s)):
    num_words_list.append(len(s[j]))
print(num_words_list)


