"""
Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.
"""



fileref = open("emotion_words.txt", "r")
reading = fileref.readlines()
j_emotions = []
spl=""
for i in reading:
    spl = i.split()
    #print(spl[1])
    #if "j" in spl:
        #j_emotions.append(spl)
for i in range(len(spl)):
    if "j" in spl[i]:
        j_emotions.append(spl)
fileref.close()



#NON è corretto!!!!