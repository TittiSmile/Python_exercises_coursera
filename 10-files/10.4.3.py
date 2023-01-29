"""
Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable 
num_lines. Do not use the len method.
"""


emotionfile = open("emotion_words.txt", "r")
num_lines=0
for i in emotionfile:
    num_lines+=1
emotionfile.close()


