"""
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words.

"""



fileref = open("emotion_words.txt", "r")
reading = fileref.read()
num_words=0
splitting_data = reading.split()
for i in reading:
    num_words=len(splitting_data)
print(num_words)
fileref.close()
