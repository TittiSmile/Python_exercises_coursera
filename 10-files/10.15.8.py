"""
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

"""

fileref = open("school_prompt.txt", "r")
three=[]
reading = fileref.readlines()
for i in reading:
    spl = i.split(" ")[2]
    three.append(spl)
print(three)
fileref.close()

