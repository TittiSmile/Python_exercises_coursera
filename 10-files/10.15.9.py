"""
Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

"""
fileref = open("emotion_words.txt", "r")
emotions=[]
reading = fileref.readlines()
for i in reading:
    spl = i.split(" ")[0]
    emotions.append(spl)
print(emotions)
fileref.close()



