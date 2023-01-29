"""
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
"""

fileref = open("school_prompt.txt", "r")
p_words = []
reading = fileref.read()
#stripping = reading.strip()
splitting = reading.split(" ")
for i in splitting:
    if "p" in i:
        p_words.append(i)
print(p_words)
fileref.close()



#c'è un problema. mi prende i \n




#versione CORRETTA!!!!
file = open("school_prompt.txt","r")
reading = file.read()
splitted_read = reading.split()
p_words=[]
for i in splitted_read:
    if "p" in i:
        p_words.append(i)
print(p_words)


file.close()
